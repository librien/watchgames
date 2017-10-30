import requests
import json
import time
import datetime
import urllib.request
import urllib
from pprint import pprint

team_name = "Washington Capitals" # Set this to your desired team (ex. Washington Capitals)
NBCSP = '590' # Set this to your local tv channel number for this network
NBCSWA = '576' # Set this to your local tv channel number for this network

todaysdate = time.strftime("%Y-%m-%d") # Get today's date to limit

api_url = ("https://statsapi.web.nhl.com/api/v1/schedule?startDate="+todaysdate+"&endDate="+todaysdate+"&expand=schedule.broadcasts.all")

data = requests.get(api_url).json()

for game in data['dates'][0]['games']:
    if (game['teams']['away']['team']['name'] == team_name) or (game['teams']['home']['team']['name'] == team_name):
        print(game['teams']['away']['team']['name'] + ' at ' + game['teams']['home']['team']['name'])
        game_time = datetime.datetime.strptime(game['gameDate'], "%Y-%m-%dT%H:%M:%SZ") # convert string to timestamp
        print(game_time)

        # Determine correct TV channel
        for broadcast in game['broadcasts']:
            if broadcast['name'] == "NBCSP":
                tv_channel = NBCSP
            elif broadcast['name'] == "NBCSWA":
                tv_channel = NBCSWA

        print(tv_channel)

current_status = urllib.request.urlopen("http://192.168.2.47:8282/hubs/harmony-hub/status").read().decode('UTF-8') # Get current status data
current_status = json.loads(current_status)
current_activity = current_status['current_activity'].items() # Get current_activity information from current_status

is_off = current_status['off']

# Check to see if harmony is off, if so, start activity
if (is_off == True):
    print(requests.post(url='http://192.168.2.47:8282/hubs/harmony-hub/activities/watchtv'))

print(is_off)
