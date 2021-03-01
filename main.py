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
mpl.rcParams['font.family'] = 'Avenir'
mpl.rcParams['font.size'] = 18
mpl.rcParams['axes.linewidth'] = 2
    
    

def main():
    # Draw basketball court
    #fig = plt.figure(figsize=(4, 3.76))
    #ax = fig.add_axes([0, 0, 1, 1])
    #ax = create_court(ax, 'black')
    #plt.show()

    #-----------------------------------------------------------
    #Search by name

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
        seasontype = 'Post Season'

    #get shot log for that season
    playerstatsdf = get_shot_chart(player['id'], seasoninput, seasontype)
    
    #print out chart




if __name__ == '__main__':
    main()
    