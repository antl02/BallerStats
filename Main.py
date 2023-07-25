import numpy as np
import streamlit as st
import pandas as pd
import pydeck as pdk
import requests
import json
# Test
st.set_page_config(
    page_title = "BallerStats",
    layout = "wide",
    menu_items = {
        'Get Help': 'https://docs.streamlit.io/',
        'About': '# Welcome to BallerStats. Here you can find all the stats you need!'
    }
)

st.title("BallerStats")
st.markdown("---")
# st.header("What is this?")

add_selectbox = st.sidebar.selectbox(
    "Select a Page",
    ["Home", "About Us", "League Stats", "Records", "NBA Market", "Members"]
)

if add_selectbox == "Home":
    st.header("Welcome to Our Site")
    st.text("Find all of the data you need about your favorite basketball players!")
    st.image("media/NBALogo.jpeg")

elif add_selectbox == "About Us":
    st.subheader("About Us")
    st.text("All the numbers at your fingertips. With Ballerstats, you will be able to know all kinds of statistics"
            " when it comes to your favorite team or player.\nGet to learn the history of the game with records. "
            "Be in the know of the market and who is on the move. Statistics will be updated game-to-game so\nyou"
            " will always know the performance of every player and team. ")

elif add_selectbox == "League Stats":
    st. header("Most Recent Games")
    response = requests.get('https://www.balldontlie.io/api/v1/games').json()

    game = response['data']
    # Creating a dataframe for the recent games
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


view = st.selectbox("Map View", ["Default", "Street", "Satellite"])
map_data = pd.DataFrame(
    np.array([[37.768009, -122.387787]]),
    columns=['lat', 'lon']
)

if view == "Default":
    st.pydeck_chart(
        pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=37.768009,
                longitude=-122.387787,
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
                latitude=37.768009,
                longitude=-122.387787,
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
                latitude=37.768009,
                longitude=-122.387787,
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

st.caption("Location of the 2019 NBA Finals: Chase Center")
