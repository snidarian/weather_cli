#!/usr/bin/python3



import requests as rq
import argparse




parser = argparse.ArgumentParser(description="Outputs 3 day forcast for given location argument")

args = parser.add_argument('location', help="city or zipcode string", type=str)

args = parser.parse_args()


result = rq.get(f'https://goweather.herokuapp.com/weather/{args.location}')


data_object = result.json()


print(data_object)

