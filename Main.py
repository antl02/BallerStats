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
    st.header("League Statistics")
    st.subheader("Most Recent Games")
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

    favorite_team = st.selectbox("Select you favorite team.",
                                 ["", "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets",
                                  "Chicago Bulls", "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets",
                                  "Detroit Pistons", "Golden State Warriors", "Houston Rockets", "Indiana Pacers",
                                  "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat",
                                  "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans",
                                  "New York Knicks", "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers",
                                  "Phoenix Suns", "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs",
                                  "Toronto Raptors", "Utah Jazz", "Washington Wizards"]
                                 )

    if favorite_team == "Atlanta Hawks":
        st.header("Atlanta Hawks")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [41, 41]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [116.9, 113.3]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Boston Celtics":
        st.header("Boston Celtics")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [57, 25]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [117.9, 111.4]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Brooklyn Nets":
        st.header("Brooklyn Nets")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [45, 37]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [113.4, 112.5]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Charlotte Hornets":
        st.header("Charlotte Hornets")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [27, 55]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [111.0, 117.2]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Chicago Bulls":
        st.header("Chicago Bulls")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [40, 42]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [113.1, 111.8]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Cleveland Cavaliers":
        st.header("Cleveland Cavaliers")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [51, 31]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [112.3, 106.9]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Dallas Mavericks":
        st.header("Dallas Mavericks")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [38, 44]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [114.2, 114.1]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Denver Nuggets":
        st.header("Denver Nuggets")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [53, 29]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [115.8, 112.5]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Detroit Pistons":
        st.header("Detroit Pistons")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [17, 65]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [110.3, 118.5]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Golden State Warriors":
        st.header("Golden State Warriors")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [44, 38]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [118.9, 117.1]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Houston Rockets":
        st.header("Houston Rockets")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [51, 31]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(22, 60)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [110.7, 118.6]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Indiana Pacers":
        st.header("Indiana Pacers")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [35, 47]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [116.3, 119.5]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Los Angeles Clippers":
        st.header("Los Angeles Clippers")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [44, 38]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [113.6, 111.6]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Los Angeles Lakers":
        st.header("Los Angeles Lakers")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [43, 39]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [117.2, 116.6]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Memphis Grizzlies":
        st.header("Memphis Grizzlies")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [51, 31]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [116.9, 113.0]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Miami Heat":
        st.header("Miami Heat")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [41, 38]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [109.5, 109.8]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Milwaukee Bucks":
        st.header("Milwaukee Bucks")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [58, 24]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [116.9, 113.3]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Minnesota Timberwolves":
        st.header("Minnesota Timberwolves")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [42, 40]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [115.8, 115.8]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "New Orleans Pelicans":
        st.header("New Orleans Pelicans")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [40, 42]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [114.4, 112.5]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "New York Knicks":
        st.header("New Your Knicks")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [47, 35]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [116.0, 113.1]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Oklahoma City Thunder":
        st.header("Oklahoma City Thunder")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [40, 42]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [117.5, 116.4]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Orlando Magic":
        st.header("Orlando Magics")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [34, 48]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [111.4, 114.0]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Philadelphia 76ers":
        st.header("Philadelphia 76ers")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [54, 28]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [115.2, 110.9]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Phoenix Suns":
        st.header("Phoenix Suns")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [45, 37]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [113.6, 111.6]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Portland Trail Blazers":
        st.header("Portland Trail Blazers")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [33, 49]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [113.4, 117.4]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Sacramento Kings":
        st.header("Sacramento Kings")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [48, 34]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [120.7, 118.1]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "San Antonio Spurs":
        st.header("San Antonio Spurs")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [22, 60]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [113.0, 123.1]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Toronto Raptors":
        st.header("Toronto Raptors")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [41, 41]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [112.9, 111.4]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Utah Jazz":
        st.header("Utah Jazz")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [37, 45]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [117.1, 118.0]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    if favorite_team == "Washington Wizards":
        st.header("Washington Wizards")
        st.subheader("2022-23 Record")
        categories = ['Wins', 'Losses']
        values = [35, 47]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('Win/Loss Record')
        ax.set_ylim(0, 82)
        plt.ylabel('Games')
        st.pyplot(fig)

        st.subheader("PPG/OPP PPG")
        categories = ['PPG', 'OPP PPG']
        values = [113.2, 114.4]
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        plt.xlabel('PPG/OPP PPG')
        ax.set_ylim(0, 150)
        plt.ylabel('Games')
        st.pyplot(fig)

    st.subheader("Current Player Statistics")
    st.info("Example: Anthony Davis")
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
            players.index += 1
            st.dataframe(players)
        elif player_name:
            st.warning("No player was found. Make sure the input format was correct.")
    except Exception:
        st.error("Failed to get the info requested. Refresh and try again.")

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
