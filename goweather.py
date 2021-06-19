#!/usr/bin/python3
# returns results from the goweather web API


import requests as rq
import argparse
import os
import json as j
from colorama import Fore


# ansi color code sequences
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
reset = Fore.RESET


# setup for argparse - grab arguments
parser = argparse.ArgumentParser(description="Outputs 3 day forcast for given location argument")

args = parser.add_argument('location', help="city or zipcode string", type=str)
args = parser.add_argument('-c', '--days-ahead', help='Specify how many days ahead the forcast should be (max 3)', type=str, default='3')

args = parser.parse_args()


result = rq.get(f'https://goweather.herokuapp.com/weather/{args.location}')


data_object = result.json()


# print(data_object)

json_string = j.dumps(data_object, indent=2, ensure_ascii=False)


# For the current weekday names list of the next three days to label for three day forcast
weekdays = {
    '0\n': ['Monday', 'Tuesday', 'Wednesday'],
    '1\n': ['Tuesday', 'Wednesday', 'Thursday'],
    '2\n': ['Wednesday', 'Thursday', 'Friday'],
    '3\n': ['Thursday', 'Friday', 'Saturday'],
    '4\n': ['Friday', 'Saturday', 'Sunday'],
    '5\n': ['Saturday', 'Sunday', 'Monday'],
    '6\n': ['Sunday', 'Monday', 'Tuesday'],
}

# display today's forecast
print(yellow)
os.system('date "+%A, %b %e"')
print(green + "Temperature: " + reset + f"{data_object['temperature']}")
print(green + "Wind: " + reset + f"{data_object['wind']}")
print(green + "description: " + reset + f"{data_object['description']}")


# determine what day of the week it is
day_of_week = os.popen('date +%w').read()
# print(f'{weekdays[day_of_week]}')
# print(day_of_week)


#print(data_object)
#print(json_string)


# if the -c flag argument is > 3, set it to 3
# print the forcast X number of days ahead (default=3)
if int(args.days_ahead) >= 3:
    args.days_ahead = '3'
else:
    pass



index = 0
for _ in range((int(args.days_ahead))):    
    print(yellow + f"\n{weekdays[day_of_week][index]}" + reset + ": ")
    print(green + "Temp: " + reset + f"{data_object['forecast'][index]['temperature']}")
    print(green + "Wind: " + reset + f"{data_object['forecast'][index]['wind']}")
    index+=1







