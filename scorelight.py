import time
from itertools import cycle
from pprint import pprint
from phue import Bridge
from rgbxy import Converter

b = Bridge('192.168.2.90')

b.connect()
team_colors = []
team_colors.append('CF132B') # Team primary color
team_colors.append('00214D') # Team secondary color
#team_colors_append('') # Team tertiary color

converter = Converter()
for i, item in enumerate(team_colors):
    xy_color = converter.hex_to_xy(item)
    team_colors[i] = xy_color


print(team_colors)
lights = []
lights.append('Basement 1')
lights.append('Basement 2')

for light in lights:
    print(b.get_light(light))

#print(b.set_light(lights, 'xy', team_colors))
c = cycle(team_colors)
for i in range(9):
    team_color = next(c)
    print(b.set_light(lights, 'xy', team_color))
    time.sleep(.75)
