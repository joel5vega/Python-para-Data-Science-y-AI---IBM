import pandas as pd
from nba_api.stats.static import teams
import matplotlib.pyplot as plt

dict_={'a':[11,21,31],'b':[12,22,32]}
df=pd.DataFrame(dict_)
print(type(df))
# print(df.head())
nba_teams = teams.get_teams()
# nba_teams[0:3]


def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict    

dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)

df_teams.head()
df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors
id_warriors=df_warriors[['id']].values[0][0]
# Tenemos ahora un número entero que puede usarse para solicitar información sobre los Warriors 
print(id_warriors)
from nba_api.stats.endpoints import leaguegamefinder
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
# print(gamefinder.get_json())
games = gamefinder.get_data_frames()[0]
print(games.head())
games_home=games [games ['MATCHUP']=='GSW vs. TOR']
games_away=games [games ['MATCHUP']=='GSW @ TOR']
print(games_away.mean()['PLUS_MINUS'])
fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()