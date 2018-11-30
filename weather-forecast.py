# -*- coding: utf-8 -*-
import pyowm
import json
from datetime import datetime

class Weather:
    def __init__(self):
        self.owm = pyowm.OWM(YOUR_API_KEY)

    def search(self, city):
        try:
	        obs = self.owm.weather_at_place(city)
	        weather = self.parse_data(obs)
	        for k, v in weather.items():
	                print(k, v)
        except:
            print('Invalid City Name')
                
        
    def parse_data(self, obs):
        w = json.loads(obs.get_weather().to_JSON())
        parsed_weather = {
            'Temperature: ' : str(w['temperature']['temp'] - 273.15) + ' °C',
            'Humdity: ' : w['humidity'],
            'Status: ' : w['status'],
            'Sunrise': datetime.fromtimestamp(w['sunrise_time']),
            'Sunset: ': datetime.fromtimestamp(w['sunset_time']),
            'Day_length: ': (w['sunset_time'] - w['sunrise_time']) / 3600,
            'Night_length: ': 24 - (w['sunset_time'] - w['sunrise_time']) / 3600
        }
        return parsed_weather

def main():
    weather = Weather()
    city = input('Enter City Name: ')
    weather.search(city)

if __name__ == '__main__':
    main()
