from nba_api.stats.endpoints import shotchartdetail
import json
import pandas as pd

def get_shot_chart(playerid, season, seasontype):
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
# write to csv file
#	df.to_csv('hehe.csv', index=False)