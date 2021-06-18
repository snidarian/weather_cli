#!/usr/bin/python3



import requests as rq
import argparse
import json as j



parser = argparse.ArgumentParser(description="Outputs 3 day forcast for given location argument")

args = parser.add_argument('location', help="city or zipcode string", type=str)
args = parser.add_argument('--c', '--days-ahead', help='Specify how many days ahead the forcast should be (max 3)', type=str, default='3')

args = parser.parse_args()


result = rq.get(f'https://goweather.herokuapp.com/weather/{args.location}')


data_object = result.json()


# print(data_object)


json_string = j.dumps(data_object, indent=2, ensure_ascii=False)


# if the -c flag argument is > 3, set it to 3
# print the forcast X number of days ahead (default=3)






print(json_string)


