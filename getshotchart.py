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
	shotchartdf = pd.DataFrame(rows)
	shotchartdf.columns = headers
	return shotchartdf

def getchart(player, seasonin, seastype):
	questions = [
		inquirer.List('charttype',
				message="What type of chart?",
				choices=['Hex Bin', 'Scatter', 'Ahead/Behind'])]

	charttype = inquirer.prompt(questions)
	# print(player, seasonin, seastype,charttype['charttype'])
	return chartmanager(player, seasonin, seastype,charttype['charttype'])

def chartmanager(player, seasonin, seastype, charttype):
	for item in seasonin:
		if (charttype == 'Hex Bin'):
			hexbinshotsmade(player,item,seastype)
		elif (charttype == 'Scatter'):
			shotsmadeplotbyshottype(player, item, seastype)
		# elif (charttype == 'Ahead/Behind'):
		# 	get_shot_data_aheadbehind(player,item,seastype)



def hexbinshotsmade(player, seasonin, seastype):
	#get shot log for that season
	playerdata = get_shot_data(player['id'], seasonin, seastype)

	# Draw basketball court
	fig = plt.figure(figsize=(7, 6))

	ax = fig.add_axes([0, 0, 1, 1])
	ax = create_court(ax, 'black')
	ax.set_title((player["full_name"] + ' Field Goals Made ' + ' '  + str(seasonin) + ' ' + str(seastype) + ' ' + 'Hex'), color='Black')
	# Plot hexbin of shots
	ax.hexbin(playerdata['LOC_X'], playerdata['LOC_Y'] + 60, gridsize=(30, 30), extent=(-300, 300, 0, 940),bins='log', cmap='Reds', facecolor='black')
	# plt.title(player["full_name"] + ' '  + str(seasonin) + ' ' + str(seastype) + ' ' + 'Hexbin')
	plt.savefig(player["full_name"] + ' '  + str(seasonin) + ' ' + str(seastype) + ' ' + 'Hexbin' + '.png')

def shotsmadeplot(player, seasonin, seastype):
	#get shot log for that season
	playerdata = get_shot_data(player['id'], seasonin, seastype)
	# Draw basketball court
	fig = plt.figure(figsize=(7, 6), facecolor='black')
	ax = fig.add_axes([0, 0, 1, .95])
	ax = create_court(ax, 'white')
	ax.set_title((player["full_name"] + ' Field Goals Made' + ' '  + str(seasonin) + ' ' + str(seastype) + ' ' + 'Scatter'), color='white')
	# Plot hexbin of shots
	ax.scatter(playerdata['LOC_X'], playerdata['LOC_Y'] + 60, c='r')
	plt.savefig(player["full_name"] + ' '  + str(seasonin) + ' ' + str(seastype) + ' ' + 'Scatter' + '.png')

def shotsmadeplotbyshottype(player, seasonin, seastype):
	#get shot log for that season
	playerdata = get_shot_data(player['id'], seasonin, seastype)
	groupbyshottype = playerdata.groupby('ACTION_TYPE')

	# Draw basketball court
	# img = plt.imread("bullscourt_15161.png")
	fig = plt.figure(figsize=(7, 6), facecolor='black')
	ax = fig.add_axes([0, 0, 1, .95])
	# ax.imshow(img, extent=[0, 0, 1, .95])
	ax = create_court(ax, 'black')
	ax.set_title((player["full_name"] + ' Field Goals Made' + ' '  + str(seasonin) + ' ' + str(seastype) + ' ' + 'Scatter'), color='white')
	for name, group in groupbyshottype:
		plt.plot(group.LOC_X, group.LOC_Y + 60, marker='o',linestyle='', markersize=12, label=name)
	plt.legend()

	# ax.scatter(playerdata['LOC_X'], playerdata['LOC_Y'] + 60, c='r')
	plt.savefig(player["full_name"] + ' '  + str(seasonin) + ' ' + str(seastype) + ' ' + 'Scatter' + '.png')
