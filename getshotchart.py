from nba_api.stats.endpoints import shotchartdetail
import inquirer
import json
import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from CreateCourt import create_court




def get_shot_data(playerid, season, seasontype):
	response = shotchartdetail.ShotChartDetail(
		team_id=0,
		player_id=playerid,
		season_nullable=season,
		season_type_all_star=seasontype)
	content = json.loads(response.get_json())
	# transform contents into dataframe
	results = content['resultSets'][0]
	headers = results['headers']
	rows = results['rowSet']
	df = pd.DataFrame(rows)
	df.columns = headers
	return df

def getchart(player, seasonin, seastype):
	questions = [
		inquirer.List('charttype',
				message="What type of chart?",
				choices=['Hex Bin', 'Scatter'])]

	charttype = inquirer.prompt(questions)
	if (charttype['charttype'] == 'Hex Bin'):
    		hexbinshotsmade(player,seasonin,seastype)
	if (charttype['charttype'] == 'Scatter'):
    		shotsmadeplot(player, seasonin, seastype)


def hexbinshotsmade(player, seasonin, seastype):
    #get shot log for that season
    playerdata = get_shot_data(player['id'], seasonin, seastype)
    
    # Draw basketball court
    fig = plt.figure(figsize=(7, 6))
	
    ax = fig.add_axes([0, 0, 1, 1])
    ax = create_court(ax, 'black')
	
    # Plot hexbin of shots
    ax.hexbin(playerdata['LOC_X'], playerdata['LOC_Y'] + 60, gridsize=(30, 30), extent=(-300, 300, 0, 940),bins='log', cmap='Reds', facecolor='black')
    plt.show()

def shotsmadeplot(player, seasonin, seastype):
    #get shot log for that season
    playerdata = get_shot_data(player['id'], seasonin, seastype)
    
    # Draw basketball court
    fig = plt.figure(figsize=(7, 6), facecolor='black')

    ax = fig.add_axes([0, 0, 1, 1])
    ax = create_court(ax, 'white')

    # Plot hexbin of shots
    ax.scatter(playerdata['LOC_X'], playerdata['LOC_Y'] + 60, color='r')
    plt.show()	
