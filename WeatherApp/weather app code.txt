import tkinter as tk
from tkinter import Image
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
from geopy import location
import requests
from uszipcode import SearchEngine


#Intialize GUI Config
app = tk.Tk()
app.geometry('1200x600')
app.configure(bg='#DDF7FF')

#Initialize Logo
logo_image = Image.open('Weather App\Media Assets\Logo.png')
main_logo = ImageTk.PhotoImage(logo_image)

#Initialize Weather Icons
sunny_image = Image.open('Weather App\Media Assets\sunny.png')
sunny_logo = ImageTk.PhotoImage(sunny_image)
rainy_image = Image.open('Weather App\Media Assets\Rain.png')
rainy_logo = ImageTk.PhotoImage(rainy_image)
lightning_image = Image.open('Weather App\Media Assets\Lightning.png')
lightning_logo = ImageTk.PhotoImage(lightning_image)
drizzle_image = Image.open('Weather App\Media Assets\Drizzle.png')
drizzle_logo = ImageTk.PhotoImage(drizzle_image)
cloudy_image = Image.open('Weather App\Media Assets\Cloud.png')
cloudy_logo = ImageTk.PhotoImage(cloudy_image)
snow_image = Image.open('Weather App\Media Assets\snow.png')
snow_logo = ImageTk.PhotoImage(snow_image)

#Initialize Logo
label = tk.Label(app, image = main_logo)
label.place(x = 20, y = 20)

def search_zip():
    zip = search_value.get()
    search = SearchEngine()
    zipcode_data = search.by_zipcode(zip)
    city = zipcode_data.major_city
    print(city)
    convert(city)

#Convert Long and Lat Function
def convert(city):
    geolocator = Nominatim(user_agent = 'bowtiedwave')
    city = geolocator.geocode(city)
    if city is not None:
        lat = city.latitude
        long = city.longitude
        print(lat,long)
        show_weather(lat,long)

def show_weather(lat,long):
    api_key = '3b7a83991095f8cffa62e8b56a54f6c1'
    weather_data = requests.get(
        f'http://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={long}&cnt=7&units=imperial&appid={api_key}%22')
    print(weather_data.json)


#Initialize Search Bar and Search Button
search_value = tk.StringVar()
search = tk.Entry(app, text = 'Input Zipcode', textvariable= search_value,font=('Ubuntu',12))
search.place(x=154, y=180, width=254, height=20)
search_button = tk.Button(app, text = 'SEARCH', bg='Black',fg='White',font=('Ubuntu',14),command=search_zip)
search_button.place(x=49,y=171,width=94,height=36,)

#Intialize Current Location Title and Data 
current_location = tk.Label(app, text = 'Select A Location',bg='#DDF7FF',fg='black',font=('Ubuntu',40,'underline'))
current_location.place(x=157,y=19)
current_location = tk.Label(app, text = '01/01/01',bg='#DDF7FF',fg='black',font=('Ubuntu',24))
current_location.place(x=157,y=80)
current_location = tk.Label(app, text = '1:27 pm',bg='#DDF7FF',fg='black',font=('Ubuntu',24))
current_location.place(x=157,y=112)

#Initialize Current Day Forecast Card and Data 
day1_forecast = tk.Label(app, bg="white", fg='black')
day1_forecast.place(x=656,y=10, width=485, height=194)
day1fc_title = tk.Label(app,text="Today's Forecast",bg='white',fg='black',font=('Ubuntu',18,'underline'))
day1fc_title.place(x=675,y=21)

#Initialize Daily Cards 
day2_forecast = tk.Label(app, bg= '#FFF4CC',fg='black')
day2_forecast.place(x=33,y=232, width=170, height=291)
    #Day Label
day2_day = tk.Label(day2_forecast,text="Tuesday",bg='#FFF4CC',fg='black',font=('Ubuntu',18,'underline','bold'))
day2_day.place(relx=0.5, y=20, anchor='center')
    #Weather Description
day2_weather = tk.Label(day2_forecast,text="Sunny",bg='#FFF4CC',fg='black',font=('Ubuntu',18,'italic',))
day2_weather.place(relx=0.5, y=60, anchor='center')
    #Weather Image Logo
day2_image = tk.Label(day2_forecast,image=sunny_logo, bg='#FFF4CC')
day2_image.place(relx=0.5, y=120, anchor='center')
    #Numerical Temp Value
day2_temp = tk.Label(day2_forecast,text="°76",bg='#FFF4CC',fg='black',font=('Ubuntu',24,'bold',))
day2_temp.place(relx=0.5, y=180, anchor='center')
    #Min/Max Temp Values
day2_minmax = tk.Label(day2_forecast,text="°76/°88",bg='#FFF4CC',fg='black',font=('Ubuntu',12))
day2_minmax.place(relx=0.5, y=220, anchor='center')


day3_forecast = tk.Label(app, bg= '#5988FF',fg='black')
day3_forecast.place(x=228,y=232, width=170, height=291)
    #Day Label
day3_day = tk.Label(day3_forecast,text="Wednesday",bg='#5988FF',fg='black',font=('Ubuntu',18,'underline','bold'))
day3_day.place(relx=0.5, y=20, anchor='center')
    #Weather Description
day3_weather = tk.Label(day3_forecast,text="Rainy",bg='#5988FF',fg='black',font=('Ubuntu',18,'italic',))
day3_weather.place(relx=0.5, y=60, anchor='center')
    #Weather Image Logo
day3_image = tk.Label(day3_forecast,image=rainy_logo, bg='#5988FF')
day3_image.place(relx=0.5, y=120, anchor='center')
    #Numerical Temp Value
day3_temp = tk.Label(day3_forecast,text="°76",bg='#5988FF',fg='black',font=('Ubuntu',24,'bold',))
day3_temp.place(relx=0.5, y=180, anchor='center')
    #Min/Max Temp Values
day3_minmax = tk.Label(day3_forecast,text="°76/°88",bg='#5988FF',fg='black',font=('Ubuntu',12))
day3_minmax.place(relx=0.5, y=220, anchor='center')


day4_forecast = tk.Label(app, bg= '#818697',fg='black')
day4_forecast.place(x=423,y=232, width=170, height=291)
    #Day Label
day4_day = tk.Label(day4_forecast,text="Thursday",bg='#818697',fg='black',font=('Ubuntu',18,'underline','bold'))
day4_day.place(relx=0.5, y=20, anchor='center')
    #Weather Description
day4_weather = tk.Label(day4_forecast,text="Lightning",bg='#818697',fg='black',font=('Ubuntu',18,'italic',))
day4_weather.place(relx=0.5, y=60, anchor='center')
    #Weather Image Logo
day4_image = tk.Label(day4_forecast,image=lightning_logo, bg='#818697')
day4_image.place(relx=0.5, y=120, anchor='center')
    #Numerical Temp Value
day4_temp = tk.Label(day4_forecast,text="°76",bg='#818697',fg='black',font=('Ubuntu',24,'bold',))
day4_temp.place(relx=0.5, y=180, anchor='center')
    #Min/Max Temp Values
day4_minmax = tk.Label(day4_forecast,text="°76/°88",bg='#818697',fg='black',font=('Ubuntu',12))
day4_minmax.place(relx=0.5, y=220, anchor='center')


day5_forecast = tk.Label(app, bg= '#C0E8F4',fg='black')
day5_forecast.place(x=618,y=232, width=170, height=291)
    #Day Label
day4_day = tk.Label(day5_forecast,text="Friday",bg='#C0E8F4',fg='black',font=('Ubuntu',18,'underline','bold'))
day4_day.place(relx=0.5, y=20, anchor='center')
    #Weather Description
day4_weather = tk.Label(day5_forecast,text="Drizzle",bg='#C0E8F4',fg='black',font=('Ubuntu',18,'italic',))
day4_weather.place(relx=0.5, y=60, anchor='center')
    #Weather Image Logo
day4_image = tk.Label(day5_forecast,image=drizzle_logo, bg='#C0E8F4')
day4_image.place(relx=0.5, y=120, anchor='center')
    #Numerical Temp Value
day4_temp = tk.Label(day5_forecast,text="°76",bg='#C0E8F4',fg='black',font=('Ubuntu',24,'bold',))
day4_temp.place(relx=0.5, y=180, anchor='center')
    #Min/Max Temp Values
day4_minmax = tk.Label(day5_forecast,text="°76/°88",bg='#C0E8F4',fg='black',font=('Ubuntu',12))
day4_minmax.place(relx=0.5, y=220, anchor='center')


day6_forecast = tk.Label(app, bg= '#DBDBDB',fg='black')
day6_forecast.place(x=813,y=232, width=170, height=291)
    #Day Label
day6_day = tk.Label(day6_forecast,text="Saturday",bg='#DBDBDB',fg='black',font=('Ubuntu',18,'underline','bold'))
day6_day.place(relx=0.5, y=20, anchor='center')
    #Weather Description
day6_weather = tk.Label(day6_forecast,text="Cloudy",bg='#DBDBDB',fg='black',font=('Ubuntu',18,'italic',))
day6_weather.place(relx=0.5, y=60, anchor='center')
    #Weather Image Logo
day6_image = tk.Label(day6_forecast,image=cloudy_logo, bg='#DBDBDB')
day6_image.place(relx=0.5, y=120, anchor='center')
    #Numerical Temp Value
day6_temp = tk.Label(day6_forecast,text="°76",bg='#DBDBDB',fg='black',font=('Ubuntu',24,'bold',))
day6_temp.place(relx=0.5, y=180, anchor='center')
    #Min/Max Temp Values
day6_minmax = tk.Label(day6_forecast,text="°76/°88",bg='#DBDBDB',fg='black',font=('Ubuntu',12))
day6_minmax.place(relx=0.5, y=220, anchor='center')



day7_forecast = tk.Label(app, bg= '#FFFFFF',fg='black')
day7_forecast.place(x=1008,y=232, width=170, height=291)
    #Day Label
day7_day = tk.Label(day7_forecast,text="Sunday",bg='#FFFFFF',fg='black',font=('Ubuntu',18,'underline','bold'))
day7_day.place(relx=0.5, y=20, anchor='center')
    #Weather Description
day7_weather = tk.Label(day7_forecast,text="Snowing",bg='#FFFFFF',fg='black',font=('Ubuntu',18,'italic',))
day7_weather.place(relx=0.5, y=60, anchor='center')
    #Weather Image Logo
day7_image = tk.Label(day7_forecast,image=snow_logo, bg='#FFFFFF')
day7_image.place(relx=0.5, y=120, anchor='center')
    #Numerical Temp Value
day7_temp = tk.Label(day7_forecast,text="°76",bg='#FFFFFF',fg='black',font=('Ubuntu',24,'bold',))
day7_temp.place(relx=0.5, y=180, anchor='center')
    #Min/Max Temp Values
day7_minmax = tk.Label(day7_forecast,text="°76/°88",bg='#FFFFFF',fg='black',font=('Ubuntu',12))
day7_minmax.place(relx=0.5, y=220, anchor='center')
app.mainloop()
