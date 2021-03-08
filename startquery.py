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
    playername = input("Search By Name: ")
    if (len(playername.split()) == 2):
        player = players.find_players_by_full_name(playername)
        
    elif(len(playername.split()) == 1):
        ln = "Last Name?"

        player = players.find_players_by_first_name(playername)
        namechoices = [d['full_name'] for d in player]
        namechoices.insert(0,ln)
        names = [
        inquirer.List('fname',
                message="Who?",
                choices= namechoices,
            ),
        ]
        fname = inquirer.prompt(names)
        if (fname['fname'] == ln):
            player = players.find_players_by_last_name(playername)
            lnamechoices = [d['full_name'] for d in player]
            lnamechoices.insert(0,ln)
            lastnames = [
                inquirer.List('lname',
                    message="Who?",
                    choices= lnamechoices,
                ),
            ]
            lname = inquirer.prompt(lastnames)
            playerl = players.find_players_by_full_name(lname['lname'])
            return playerl[0]
        else:
          return  players.find_players_by_full_name(fname['fname'])[0]     
    else:
        return
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





