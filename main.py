# Import packages
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.static import players
import json
import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from CreateCourt import create_court

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

    val = input("Who are you looking for: ")
    lbj = players.find_players_by_full_name(val)
    print(lbj)


if __name__ == '__main__':
    main()
    