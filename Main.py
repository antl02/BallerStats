from datetime import date

import numpy as np
import streamlit as st
import pandas as pd
import pydeck as pdk
import requests
import matplotlib.pyplot as plt
import json

# Test 3 for Video
st.set_page_config(
    page_title="BallerStats",
    layout="wide",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/',
        'About': '# Welcome to BallerStats. Here you can find all the stats you need!'
    }
)

st.title("BallerStats")
st.markdown("---")
# st.header("What is this?")

add_selectbox = st.sidebar.selectbox(
    "Select a Page",
    ["Home", "About Us", "League Stats", "Misc Info"]
)
response = requests.get('https://www.balldontlie.io/api/v1/games').json()
if add_selectbox == "Home":
    st.header("Welcome to Our Site")
    st.text("Find all of the data you need about the NBA and its players up to the 2019 season!")
    st.image("media/NBALogo.jpeg")

elif add_selectbox == "About Us":
    st.subheader("About Us")
    st.text("All the numbers at your fingertips. With Ballerstats, you will be able to know all kinds of statistics"
            " when it comes to your favorite team or player.\nGet to learn the history of the game with records. "
            "Be in the know of the market and who is on the move. Statistics will be updated game-to-game so\nyou"
            " will always know the performance of every player and team. ")

elif add_selectbox == "League Stats":
    st.header("League Statistics")

    game = response['data']
    # Creating a dataframe for the recent games
    col1, col2, col3 = st.columns(3)
    st.subheader("Most Recent Games")
    recent_games = pd.DataFrame(
        {
            "Date": [game[0]['date'][0:10],
                     game[1]['date'][0:10],
                     game[2]['date'][0:10],
                     game[3]['date'][0:10],
                     game[4]['date'][0:10]],

            "Home Team": [game[0]['home_team']['name'],
                          game[1]['home_team']['name'],
                          game[2]['home_team']['name'],
                          game[3]['home_team']['name'],
                          game[4]['home_team']['name']],

            "Home Team Score": [game[0]['home_team_score'],
                                game[1]['home_team_score'],
                                game[2]['home_team_score'],
                                game[3]['home_team_score'],
                                game[4]['home_team_score']],

            "Away Team": [game[0]['visitor_team']['name'],
                          game[1]['visitor_team']['name'],
                          game[2]['visitor_team']['name'],
                          game[3]['visitor_team']['name'],
                          game[4]['visitor_team']['name']],

            "Away Team Score": [game[0]['visitor_team_score'],
                                game[1]['visitor_team_score'],
                                game[2]['visitor_team_score'],
                                game[3]['visitor_team_score'],
                                game[4]['visitor_team_score']]
        }
    )
    recent_games = recent_games.sort_values(by=['Date'], ascending=False, ignore_index=True)  # Sorts table
    recent_games.index += 1
    # Displaying the dataframe
    st.dataframe(recent_games)

    # Adeel: NBA Games by Date
    st.subheader("NBA Games by Date")
    max_date_str = "2019-06-13"  # Maximum date available in the date input widget
    max_date = date.fromisoformat(max_date_str)
    selected_date = st.date_input("Select a date", value=None)

    if selected_date and selected_date <= max_date:
        formatted_date = selected_date.strftime("%Y-%m-%d")

        base_url = "https://www.balldontlie.io/api/v1/games"
        response = requests.get(f"{base_url}?dates[]={formatted_date}")
        data = response.json()

        if "data" in data:
            games = data["data"]
            # Filter out games with dates after 6/13/2019
            filtered_games = [game for game in games if game["date"] <= "2019-06-13T00:00:00.000Z"]

            if filtered_games:
                #st.subheader(f"Games on {formatted_date}:")
                for game in filtered_games:
                    home_team = game["home_team"]["full_name"]
                    visitor_team = game["visitor_team"]["full_name"]
                    home_score = game["home_team_score"]
                    visitor_score = game["visitor_team_score"]
                    st.write(f"{home_team} {home_score} - {visitor_team} {visitor_score}")
            else:
                st.write(f"No games found on or before {formatted_date}")
        else:
            st.write(f"Error fetching data for {formatted_date}")
    elif selected_date and selected_date > max_date:
        st.warning("Please select a date on or before 06/13/2019")

    st.subheader("Most Points Per Game")
    col1, col2, col3 = st.columns(3)
    # Adeel's Chart
    with col2:

        players = {
            "James Harden": 192,
            "Paul George": 172,
            "Giannis Antetokounmpo": 15,
            "Joel Embiid": 145,
            "Stephen Curry": 115
        }

        season_year = 2018
        ppg_data = []

        base_url = "https://www.balldontlie.io/api/v1/season_averages"

        for player_name, player_id in players.items():
            # Make the API call to get player's season averages
            try :
                response = requests.get(f"{base_url}?season={season_year}&player_ids[]={player_id}")
                data = response.json()
            except Exception:
                st.error("Failed to get the info requested. Refresh and try again.")


            if "data" in data:
                season_averages = data["data"][0]
                ppg_average = season_averages["pts"]
                ppg_data.append((player_name, ppg_average))
            else:
                st.write(f"Data not available for {player_name} for the specified season.")

        ppg_data.sort(key=lambda x: x[1], reverse=True)

        # Define custom colors for the bars
        bar_colors = ['red', 'blue', 'green', 'purple', 'gold', 'orange']

        # Allow the user to select a color using the select_slider
        selected_color = st.radio('Select Bar Color', options=bar_colors)

        plt.figure(figsize=(10, 6))
        # Use the selected_color variable to specify the color for the bars
        plt.bar([x[0] for x in ppg_data[:5]], [x[1] for x in ppg_data[:5]], color=selected_color)
        plt.xlabel("Player")
        plt.ylabel("Points Per Game (PPG) Average")
        plt.title(f"Top 5 Players (PPG) - {season_year} Season")
        plt.xticks(rotation=45)
    with col1:
        st.pyplot(plt)

    st.subheader("Current Player Statistics")
    st.info("Look for a player and choose what to show! Format Examples: Anthony Davis  |  Lebron  | Curry")

    check_gp = st.checkbox("Games Played")
    check_mins = st.checkbox("Average Minutes (Avg Mins)")
    check_fgm = st.checkbox("Average Field Goals Made (Avg FGM)")

    player_name = st.text_input("Player Name")
    url = "https://www.balldontlie.io/api/v1/players/"
    parameters = {'page': 0, 'per_page': 100, 'search': player_name}
    try:
        response = requests.get(url, params=parameters).json()
        names = []
        teams = []
        # conferences = []
        # divisions = []
        positions = []

        games_played = []
        avg_mins = []
        avg_fgm = []

        if len(response['data']) > 0 and player_name:
            for player in response['data']:
                names.append(player['first_name'] + " " + player['last_name'])
                teams.append(player['team']['name'])
                # conferences.append(player['team']['conference'])
                # divisions.append(player['team']['division'])
                positions.append(player['position'])

                url = "https://www.balldontlie.io/api/v1/season_averages?player_ids[]=" + str(player['id'])
                response = requests.get(url).json()
                if len(response['data']) > 0:
                    playerStats = response['data'][0]
                    games_played.append(playerStats['games_played'])
                    avg_mins.append(playerStats['min'])
                    avg_fgm.append(playerStats['fgm'])
                else:
                    games_played.append("0")
                    avg_mins.append("0")
                    avg_fgm.append("0")

            if check_gp and check_mins and check_fgm:
                players = pd.DataFrame(
                    {
                        "Player": names,
                        "Team": teams,
                        # "Conference": conferences,
                        # "Division": divisions,
                        "Position": positions,
                        "Games Played": games_played,
                        "Avg Mins": avg_mins,
                        "Avg FGM": avg_fgm
                    }
                )
            elif check_gp and check_mins:
                players = pd.DataFrame(
                    {
                        "Player": names,
                        "Team": teams,
                        # "Conference": conferences,
                        # "Division": divisions,
                        "Position": positions,
                        "Games Played": games_played,
                        "Avg Mins": avg_mins
                    }
                )
            elif check_mins and check_fgm:
                players = pd.DataFrame({
                        "Player": names,
                        "Team": teams,
                        # "Conference": conferences,
                        # "Division": divisions,
                        "Position": positions,
                        "Avg Mins": avg_mins,
                        "Avg FGM": avg_fgm
                    }
                )
            elif check_gp and check_fgm:
                players = pd.DataFrame({
                        "Player": names,
                        "Team": teams,
                        # "Conference": conferences,
                        # "Division": divisions,
                        "Position": positions,
                        "Games Played": games_played,
                        "Avg FGM": avg_fgm
                    }
                )
            elif check_gp:
                players = pd.DataFrame(
                    {
                        "Player": names,
                        "Team": teams,
                        # "Conference": conferences,
                        # "Division": divisions,
                        "Position": positions,
                        "Games Played": games_played
                    }
                )
            elif check_mins:
                players = pd.DataFrame(
                    {
                        "Player": names,
                        "Team": teams,
                        # "Conference": conferences,
                        # "Division": divisions,
                        "Position": positions,
                        "Avg Mins": avg_mins
                    }
                )
            elif check_fgm:
                players = pd.DataFrame(
                    {
                        "Player": names,
                        "Team": teams,
                        # "Conference": conferences,
                        # "Division": divisions,
                        "Position": positions,
                        "Avg FGM": avg_fgm
                    }
                )
            else:
                players = pd.DataFrame(
                    {
                        "Player": names,
                        "Team": teams,
                        # "Conference": conferences,
                        # "Division": divisions,
                        "Position": positions
                    }
                )
            players.index += 1
            st.dataframe(players)
        elif player_name:
            st.warning("No player was found. Make sure the input format was correct.")
    except Exception:
        st.error("Failed to get the info requested. Refresh and try again.")

elif add_selectbox == 'Misc Info':
    st.header("Miscellaneous Info")
    st.subheader("Does Height Matter?")
    st.text("There is often a debate between the difference height can make in the sport of basketball.\n"
            "To provide you with some evidence for supporting your answer to that question, here's the "
            "heights of the top 5 players.")
    # Top Players Heights Chart
    top_players = []
    url = "https://www.balldontlie.io/api/v1/players/"
    try:
        response = requests.get(url, params={'search': 'Lebron James'}).json()
        top_players.append(response)

        response = requests.get(url, params={'search': 'Kevin Durant'}).json()
        top_players.append(response)

        response = requests.get(url, params={'search': 'Anthony Davis'}).json()
        top_players.append(response)

        response = requests.get(url, params={'search': 'Stephen Curry'}).json()
        top_players.append(response)

        response = requests.get(url, params={'search': 'James Harden'}).json()
        top_players.append(response)
    except Exception as e:
        st.error("Error: Information could not be reached.")

    heights = [(top_players[0]['data'][0]['height_feet'] * 12) + top_players[0]['data'][0]['height_inches'],
               (top_players[1]['data'][0]['height_feet'] * 12) + top_players[1]['data'][0]['height_inches'],
               (top_players[2]['data'][0]['height_feet'] * 12) + top_players[2]['data'][0]['height_inches'],
               (top_players[3]['data'][0]['height_feet'] * 12) + top_players[3]['data'][0]['height_inches'],
               (top_players[4]['data'][0]['height_feet'] * 12) + top_players[4]['data'][0]['height_inches']]

    categories = ['Lebron James', 'Kevin Durant', 'Anthony Davis', 'Stephen Curry', 'James Harden']
    values = [heights[0], heights[1], heights[2], heights[3], heights[4]]

    fig, ax = plt.subplots(figsize=(2, 2))
    ax.bar(categories, values, width=0.2)

    plt.xlabel('Players')
    ax.set_ylim(70, 90)
    plt.ylabel('Height (in)')
    plt.tick_params(axis='x', labelsize=3)
    plt.tick_params(axis='y', labelsize=5)

    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig)

    st.subheader("Our Secret NBA Favorites 2018 - 2019 Season Averages")
    players = {
        "LeBron James": 237,
        "James Harden": 192,
        "Paul George": 172,
        "Giannis Antetokounmpo": 15,
        "Joel Embiid": 145,
        "Stephen Curry": 115
    }

    player_name = st.select_slider("Select a player:", list(players.keys()), )
    st.markdown("---")

    player_id = players[player_name]
    season_year = 2020  # You can set a default season year here or add another input to let the user choose the year.

    base_url = "https://www.balldontlie.io/api/v1/season_averages"
    response = requests.get(f"{base_url}?season={season_year}&player_ids[]={player_id}")
    data = response.json()

    if "data" in data:
        player_data = data["data"][0]
        st.write(f"**{player_name}**")

        st.write(f"Games Played: {player_data['games_played']}")
        st.write(f"Points Per Game (PPG): {player_data['pts']}")
        st.write(f"Assists Per Game (APG): {player_data['ast']}")
        st.write(f"Rebounds Per Game (RPG): {player_data['reb']}")
        # Add more stats as needed
    else:
        st.write(f"No data available for {player_name} for the specified season.")

    # NBA Finals section
    st.subheader("NBA Finals Locations")
    st.text("The annual NBA Finals are hosted at the home-town arenas of the final contenders.")
    col1, col2, col3, col4 = st.columns(4)

    loc_lat = 37.750328
    loc_lon = -122.203300
    with col1:
        st.caption("San Francisco, California")
        oracle_loc = st.button("Oracle Arena")
        if oracle_loc:
            loc_lat = 37.750328
            loc_lon = -122.203300

    with col2:
        st.caption("Toronto, Canada")
        scotia_loc = st.button("Scotiabank Arena")
        if scotia_loc:
            loc_lat = 43.643475
            loc_lon = -79.379379

    with col3:
        view = st.selectbox("Map View", ["Default", "Street", "Satellite"])
        map_data = pd.DataFrame(
            np.array([[37.750328, -122.203300], [43.643475, -79.379379]]),
            columns=['lat', 'lon']
        )

    if view == "Default":
        st.pydeck_chart(
            pdk.Deck(
                map_style=None,
                initial_view_state=pdk.ViewState(
                    latitude=loc_lat,
                    longitude=loc_lon,
                    zoom=11,
                    pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        "ScatterplotLayer",
                        data=map_data,
                        get_position="[lon, lat]",
                        get_color="[200, 30, 0, 160]",
                        get_radius=200,
                    ),
                ],
            )
        )
    elif view == "Street":
        st.pydeck_chart(
            pdk.Deck(
                map_style='mapbox://styles/mapbox/streets-v12',
                initial_view_state=pdk.ViewState(
                    latitude=loc_lat,
                    longitude=loc_lon,
                    zoom=11,
                    pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        "ScatterplotLayer",
                        data=map_data,
                        get_position="[lon, lat]",
                        get_color="[200, 30, 0, 160]",
                        get_radius=200,
                    ),
                ],
            )
        )
    elif view == "Satellite":
        st.pydeck_chart(
            pdk.Deck(
                map_style='mapbox://styles/mapbox/satellite-streets-v12',
                initial_view_state=pdk.ViewState(
                    latitude=loc_lat,
                    longitude=loc_lon,
                    zoom=11,
                    pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        "ScatterplotLayer",
                        data=map_data,
                        get_position="[lon, lat]",
                        get_color="[200, 30, 0, 160]",
                        get_radius=200,
                    ),
                ],
            )
        )

    st.caption("Locations of the 2019 NBA Finals")
