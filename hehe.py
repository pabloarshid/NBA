from nba_api.stats.endpoints import shotchartdetail
import json

response = shotchartdetail.ShotChartDetail(
	team_id=0,
	player_id=201935,
	season_nullable='2018-19',
	season_type_all_star='Regular Season'
)

content = json.loads(response.get_json())

import pandas as pd

# transform contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows)
df.columns = headers

# write to csv file
df.to_csv('hehe.csv', index=False)