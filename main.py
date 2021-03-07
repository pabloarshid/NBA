from nba_api.stats.endpoints import shotchartdetail

import json
import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# General plot parameters
mpl.rcParams['font.size'] = 18
mpl.rcParams['axes.linewidth'] = 2 

from startquery import startquery

def main():   
    startquery()

if __name__ == '__main__':
    main()
    