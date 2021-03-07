# Import packages
from nba_api.stats.static import players
import inquirer
import json
import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from CreateCourt import create_court
from getshotchart import getchart

  
def startquery():
    #Get the player info
    player = getplayer()
    
    #what season and season type
    seasoninput, seasontype = get_season()
    
    #get shot log for that season
    getchart(player,seasoninput, seasontype)

def getplayer():
    #Get the player info
    playername = input("Who are you looking for: ")
    player = players.find_players_by_full_name(playername)
    player = player[0]
    return player

def get_season():
    #what season and season type
    seasoninput = input("For what season (YYYY-YY): ")

    questions = [
    inquirer.List('seasontype',
                message="What type of Season?",
                choices=['Regular Season', 'Pre Season', 'Playoffs', 'All Star'],
            ),
    ]
    seasontype = inquirer.prompt(questions)

    return seasoninput, seasontype['seasontype']





