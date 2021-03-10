from nba_api.stats.endpoints import shotchartdetail

import json
import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# General plot parameters
mpl.rcParams['font.size'] = 10
mpl.rcParams['axes.linewidth'] = 2 
mpl.rcParams['text.color'] = 'w'

from startquery import startquery

def main():   
    startquery()

if __name__ == '__main__':
    main()
    