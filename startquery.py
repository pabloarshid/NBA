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
    # seasoninput, seasontype = get_season()
    seasoninput, seasontype= get_season()
    # print(seasoninput)

    #get shot log for that season
    getchart(player,seasoninput, seasontype)

def getplayer():
    #Get the player info
    playername = input("Search By Name: ")
    if (len(playername.split()) == 2):
        player = players.find_players_by_full_name(playername)
        player = player[0]
        return player
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


def get_season():
    #what season and season type
    #First ask single season or single season over years.
    stattype = season_chart_type()
    questions = [
        inquirer.List('seasontype',
        message="What type of Season?",
            choices=['Regular Season', 'Pre Season', 'Playoffs', 'All Star'],
                ),
            ]
    seasontype = inquirer.prompt(questions)
    if (stattype == 'Single Season'):
        seasonlist = []
        seasoninput = input("What season (YYYY-YY): ")
        seasonlist.append(seasoninput)
        return seasonlist, seasontype['seasontype']
    else:
        startseason = input("Start Season (YYYY-YY): ")
        endseason = input("End Season(YYYY-YY): ")
        seasonlist = multiple_seasons(startseason,endseason)
        return seasonlist, seasontype['seasontype']
    return




def season_chart_type():
    durationchoices = ['Single Season', 'Multiple Seasons']
    questions = [
    inquirer.List('seasontype',
                message="Single Season or Season over Season: ",
                choices=durationchoices,
            ),
    ]
    seasontype = inquirer.prompt(questions)

    return seasontype['seasontype']

def multiple_seasons(start, end):
    seasonlist = []
    seasonlist.append(start)
    splitstart = start.split("-")
    splitend = end.split("-")
    splitstartints = [int(item) for item in splitstart]
    splitendints = [int(item) for item in splitend]


    while(splitstartints[0] != splitendints[0]):
        splitstartints = [item+1 for item in splitstartints]
        if (splitstartints[1] < 10):
            tempstr = '0' + str(splitstartints[1])
        else:
            tempstr = str(splitstartints[1])
        tempseason = str(splitstartints[0]) + "-" + tempstr
        seasonlist.append(tempseason)
    return seasonlist
