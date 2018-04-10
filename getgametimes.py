import requests
import json
import time
import datetime
import urllib
from pprint import pprint

nhl_team_name = "Washington Capitals" # Set this to your desired NHL team including city and team name (ex. Washington Capitals)
mlb_team_name = "Nationals" # Set this to your desired MLB team including just team name (ex. Nationals)
nba_team_name = "Wizards" # Set this to your desired NBA team including just team name (ex. Wizards)
nfl_team_name = "WAS" # Set this to two or three letter abbreviation for your desired NFL team (ex. WAS, NE)

tv_channels = {} # Create new dict for TV channels and add name / numbers for networks
tv_channels['NBCSP'] = '590'
tv_channels['NBCSWA'] = '576'
tv_channels['FOX'] = '505'
tv_channels['TBS'] = '552'
tv_channels['ESPN'] = '570'
tv_channels['MASN'] = '577'
tv_channels['MASN2'] = '579'

default_tv_channel = '576' # Set default TV channel

todaysdate = time.strftime("%Y-%m-%d") # Get today's date to limit

class Game(object):
    '''
    Object for controlling Harmony hub schedule and channel

    Attributes:
        home_team_name
        away_team_name
        game_time
        broadcast
    '''

    def __init__(self, home_team_name, away_team_name, game_time, broadcast):
        self.home_team = home_team
        self.away_team = away_team
        self.game_time = game_time
        self.broadcast = broadcast

    def find_broadcast(*args):
        game_broadcasts = []
        for arg in args:
            game_broadcasts.append(arg)
        game_broadcast = set(tv_channels.keys()).intersection(game_broadcasts)
        for channel in game_broadcast:
            return channel
            break

def find_broadcast(broadcasts):
        broadcast = set(tv_channels.keys()).intersection(broadcasts)
        for channel in broadcast:
            return channel
            break

def get_nba_games(team_name):
    '''
    Retrieves games from NBA schedule
    '''
    api_url = ('https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2017/league/00_full_schedule_week.json')


def get_nfl_games(team_name):
    '''
    Retrieves games from NFL schedule
    '''
    api_url = ("http://www.nfl.com/liveupdate/scores/scores.json")


def get_mlb_games(team_name, todaysdate):
    ###
    # Retrieves games from MLB schedule
    ###
    day = datetime.datetime.strptime(todaysdate, '%Y-%m-%d').strftime('%d')
    month = datetime.datetime.strptime(todaysdate, '%Y-%m-%d').strftime('%m')
    year = datetime.datetime.strptime(todaysdate, '%Y-%m-%d').strftime('%Y')

    api_url = ("http://mlb.mlb.com/gdcross/components/game/mlb/year_"+year+"/month_"+month+"/day_"+day+"/master_scoreboard.json")
    #api_url = ("http://mlb.mlb.com/gdcross/components/game/mlb/year_2017/month_10/day_09/master_scoreboard.json")
    data = requests.get(api_url).content.decode('UTF-8')
    data = json.loads(data)
    try:
        for game in data['data']['games']['game']:
            if (game['home_team_name'] == team_name) or (game['away_team_name'] == team_name):
                home_team = game['home_team_name']
                away_team = game['away_team_name']
                broadcasts = []
                broadcasts.append(game['broadcast']['away']['tv'])
                broadcasts.append(game['broadcast']['home']['tv'])
                for broadcast in game['broadcast']:
                    #broadcasts.append(broadcast['tv'])
                    pass
                game_time_str = game['original_date'] + ' at ' + game['time']

    except TypeError:
        # Handle exception when there is only one game on schedule
        if (data['data']['games']['game']['home_team_name'] == team_name) or (data['data']['games']['game']['away_team_name'] == team_name):
            home_team = data['data']['games']['game']['home_team_name']
            away_team = data['data']['games']['game']['away_team_name']
            broadcasts = []
            broadcasts.append(data['data']['games']['game']['broadcast']['away']['tv'])
            broadcasts.append(data['data']['games']['game']['broadcast']['home']['tv'])
            for broadcast in data['data']['games']['game']['broadcast']:
                #broadcasts.append(broadcast['tv'])
                pass

            game_time_str = data['data']['games']['game']['original_date'] + ' at ' + data['data']['games']['game']['time']

    except KeyError:
        game_time_str = False

    finally:
        if game_time_str:
            broadcast = find_broadcast(broadcasts)

            print(away_team + " at " + home_team)
            print(game_time_str + " on " + broadcast)
        else:
            print("No MLB games scheduled today")

def get_nhl_games(team_name, todaysdate):
    '''
    Retrieves games from NHL schedule
    '''
    api_url = ("https://statsapi.web.nhl.com/api/v1/schedule?startDate="+todaysdate+"&endDate="+todaysdate+"&expand=schedule.broadcasts.all")
    #api_url = ("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2017-10-29&endDate=2017-10-29&expand=schedule.broadcasts.all")

    data = requests.get(api_url).json()

    try:
        for game in data['dates'][0]['games']:
            if (game['teams']['away']['team']['name'] == team_name) or (game['teams']['home']['team']['name'] == team_name):
                home_team = game['teams']['away']['team']['name']
                away_team = game['teams']['home']['team']['name']
                game_datetime = datetime.datetime.strptime(game['gameDate'], "%Y-%m-%dT%H:%M:%SZ") # convert string to timestamp
                game_time_str = game_datetime.strftime('%Y-%m-%d') + ' at ' + game_datetime.strftime('%H:%M')

                broadcasts = []
                for broadcast in game['broadcasts']:
                    broadcasts.append(broadcast['name'])

                broadcast = find_broadcast(broadcasts)
        try:
            print(away_team + ' at ' + home_team)
            print(game_time_str + ' on ' + broadcast)
        except NameError:
            print("No NHL games scheduled today")

    except Exception as e:
        print(e)

print(get_mlb_games(mlb_team_name, todaysdate))
print(get_nhl_games(nhl_team_name, todaysdate))
