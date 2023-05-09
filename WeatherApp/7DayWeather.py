import requests
from tkinter import *
import math
from pprint import pprint

# Set up API request URL
API_key = "{enter key}"
base_url = "http://api.openweathermap.org/data/forecast/daily?"

zip_code = input("Enter a Zip code and country code: ")
Final_url = base_url + "appid=" + API_key + "&zip=" + zip_code

weather_data = requests.get(Final_url).json()

print("\nCurrent Weather Data Of " + zip_code + ":\n")
pprint(weather_data)
print(Final_url)
