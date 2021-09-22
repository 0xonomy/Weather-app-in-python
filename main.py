from tkinter import *
from tkinter import messagebox
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
api_key = 'cef41745b2f831d0555b035ff5b7247f'

def get_weather(city):
    result=requests.get(url.format(city, api_key))
    if result:
        json = result.json()

        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = temp_celsius * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        
        final = (city, country, temp_celsius, temp_fahrenheit, icon, weather)
        return final
    else:
        return None


global img
def search():
    global image
    city = input.get()
    weather = get_weather(city)
    if weather:
        location_label['text'] = f'{weather[0]}, {weather[1]}'
        temp_label['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
        weather_label['text'] = weather[5]
    else:
        messagebox.showerror('Error', f'Cannot find city {city}')


root=Tk()

root.title("Weather")
root.geometry("700x350")

input = Entry(root, border=2)
input.pack()

text = Button(root, text="Gey Weatherz", width=14, border=1, command=search)
text.pack()

location_label = Label(root, text="", font="Bold, 19")
location_label.pack()

temp_label = Label(root, text="")
temp_label.pack()

weather_label = Label(root, text="")
weather_label.pack()

root.mainloop()