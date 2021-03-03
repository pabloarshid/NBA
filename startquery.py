# Import packages
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.static import players
import json
import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from CreateCourt import create_court
from getshotchart import get_shot_chart

# General plot parameters
mpl.rcParams['font.size'] = 18
mpl.rcParams['axes.linewidth'] = 2 
  
def startquery():
    #Get the player info
    playername = input("Who are you looking for: ")
    player = players.find_players_by_full_name(playername)
    player = player[0]
    
    #what season and season type
    seasoninput = input("For what season (YYYY-YY): ")
    seasontype = input("Regular Season or Post Season (1/2): ")
    if (seasontype == "1"):
        seasontype = 'Regular Season'
    else:
        seasontype = 'Playoffs'

    #get shot log for that season
    playerdata = get_shot_chart(player['id'], seasoninput, seasontype)
    print(playerdata)
    
    # Draw basketball court
    fig = plt.figure(figsize=(8, 7.5))
    ax = fig.add_axes([0, 0, 1, 1])
    ax = create_court(ax, 'black')

    # Plot hexbin of shots
    ax.hexbin(playerdata['LOC_X'], playerdata['LOC_Y'] + 60, gridsize=(30, 30), extent=(-300, 300, 0, 940),bins='log', cmap='Blues')
    plt.show()
