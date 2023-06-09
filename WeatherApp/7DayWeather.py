import requests
from tkinter import *
import math
from pprint import pprint

# Set up API request URL
API_key = "3b7a83991095f8cffa62e8b56a54f6c1"
base_url = "http://api.openweathermap.org/data/forecast/daily?"

zip_code = input("Enter a Zip code and country code: ")
Final_url = base_url + "appid=" + API_key + "&zip=" + zip_code

weather_data = requests.get(Final_url).json()

print("\nCurrent Weather Data Of " + zip_code + ":\n")
pprint(weather_data)
print(Final_url)

# create a function that will show weather data for 7 days

def show_weather():
        for i in range(7):
        day = weather_data['list'][i]
        date = day['dt']
        date = math.floor(date)
        date = str(date)
        date = date[0:10]
        temp = day['temp']['day']
        temp = math.floor(temp)
        temp = str(temp)
        temp = temp + "°F"
        weather = day['weather'][0]['main']
        print("\nDate: " + date)
        print("Temperature: " + temp)
        print("Weather: " + weather)


