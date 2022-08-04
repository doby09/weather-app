from create_file import create_csv
from tkinter import *
from tkinter import messagebox
import requests
import os
from datetime import datetime

api_key = os.environ['curent_weather_data']
url = "http://api.weatherbit.io/v2.0/current?city={}&key={}"
url_forecast = "http://api.weatherbit.io/v2.0/forecast/daily?city={}&days=7&key={}"

def get_weather(city):
    """
    :goal: Makes an API request and returns info.
    :param city: The city name for which to see the weather.
    :type city: str
    :return: Current weather info.
    :rtype: tuple(str, str, float, str, str, float)
    """
    result = requests.get(url.format(city, api_key))
    if result:
        api_data = result.json()
        # {City, Country, temperature, weather, icon, wind speed}
        city = api_data['data'][0]['city_name']
        country = api_data['data'][0]['country_code']
        temp_celsius = api_data['data'][0]['temp']
        weather = api_data['data'][0]['weather']['description']
        icon = api_data['data'][0]['weather']['icon']
        wind_spd = api_data['data'][0]['wind_spd']
        final = (city, country, temp_celsius, weather, icon, wind_spd)
        return final
    else:
        return None

def get_forecast(city):
    """
    :goal: Makes an API request and returns info.
    :param city: The city name for which to see the forecast.
    :type city: str
    :return: The weather forecast info.
    :rtype: tuple(str, str, float, str, str, float)
    """
    result_1 = requests.get(url_forecast.format(city, api_key))
    if result_1:
        api_data = result_1.json()
        # {City, Country, temperature and weather for 7 days}
        city = api_data['city_name']
        country = api_data['country_code']

        temp_celsius_0 = api_data['data'][0]['temp']
        weather_0 = api_data['data'][0]['weather']['description']
        wind_spd_0 = api_data['data'][0]['wind_spd']

        temp_celsius_1 = api_data['data'][1]['temp']
        weather_1 = api_data['data'][1]['weather']['description']
        wind_spd_1 = api_data['data'][1]['wind_spd']

        temp_celsius_2 = api_data['data'][2]['temp']
        weather_2 = api_data['data'][2]['weather']['description']
        wind_spd_2 = api_data['data'][2]['wind_spd']

        temp_celsius_3 = api_data['data'][3]['temp']
        weather_3 = api_data['data'][3]['weather']['description']
        wind_spd_3 = api_data['data'][3]['wind_spd']

        temp_celsius_4 = api_data['data'][4]['temp']
        weather_4 = api_data['data'][4]['weather']['description']
        wind_spd_4 = api_data['data'][4]['wind_spd']

        temp_celsius_5 = api_data['data'][5]['temp']
        weather_5 = api_data['data'][5]['weather']['description']
        wind_spd_5 = api_data['data'][5]['wind_spd']

        temp_celsius_6 = api_data['data'][6]['temp']
        weather_6 = api_data['data'][6]['weather']['description']
        wind_spd_6 = api_data['data'][6]['wind_spd']

        final = (city, country, temp_celsius_0, weather_0, temp_celsius_1, weather_1, temp_celsius_2, weather_2, temp_celsius_3, weather_3, temp_celsius_4, weather_4, temp_celsius_5, weather_5, temp_celsius_6, weather_6, wind_spd_0, wind_spd_1, wind_spd_2, wind_spd_3, wind_spd_4, wind_spd_5, wind_spd_6)
        columns = ['temperature', 'description', 'wind speed']
        rows = [[final[2], final[3], final[16]], [final[4], final[5], final[17]], [final[6], final[7], final[18]], [final[8], final[9], final[19]], [final[10], final[11], final[20]], [final[12], final[13], final[21]], [final[14], final[15], final[22]]]
        create_csv('data.csv', 'write', columns, rows)
        return final
    else:
        return None

def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        img['file'] = f'C:\\Users\\mihai\\PycharmProjects\\weather_app\\weather_icons\\{weather[4]}.png'
        temp_lbl['text'] = '{:.2f} C'.format(weather[2])
        weather_lbl['text'] = weather[3]
        wind_speed_lbl['text'] = '{:.2f}'.format(weather[5]),'km/h'
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

def forecast():

    city = city_text.get()
    weather_forecast = get_forecast(city)
    if weather_forecast:
        location_lbl['text'] = '{}, {}'.format(weather_forecast[0], weather_forecast[1])
        temp_lbl_0['text'] = '{:.2f}'.format(weather_forecast[2])
        temp_lbl_1['text'] = '{:.2f}'.format(weather_forecast[4])
        temp_lbl_2['text'] = '{:.2f}'.format(weather_forecast[6])
        temp_lbl_3['text'] = '{:.2f}'.format(weather_forecast[8])
        temp_lbl_4['text'] = '{:.2f}'.format(weather_forecast[10])
        temp_lbl_5['text'] = '{:.2f}'.format(weather_forecast[12])
        temp_lbl_6['text'] = '{:.2f}'.format(weather_forecast[14])
        weather_lbl_0['text'] = weather_forecast[3]
        weather_lbl_1['text'] = weather_forecast[5]
        weather_lbl_2['text'] = weather_forecast[7]
        weather_lbl_3['text'] = weather_forecast[9]
        weather_lbl_4['text'] = weather_forecast[11]
        weather_lbl_5['text'] = weather_forecast[13]
        weather_lbl_6['text'] = weather_forecast[15]
        wind_speed_lbl_0['text'] = '{:.2f}'.format(weather_forecast[16]), 'km/h'
        wind_speed_lbl_1['text'] = '{:.2f}'.format(weather_forecast[17]), 'km/h'
        wind_speed_lbl_2['text'] = '{:.2f}'.format(weather_forecast[18]), 'km/h'
        wind_speed_lbl_3['text'] = '{:.2f}'.format(weather_forecast[19]), 'km/h'
        wind_speed_lbl_4['text'] = '{:.2f}'.format(weather_forecast[20]), 'km/h'
        wind_speed_lbl_5['text'] = '{:.2f}'.format(weather_forecast[21]), 'km/h'
        wind_speed_lbl_6['text'] = '{:.2f}'.format(weather_forecast[22]), 'km/h'
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

app = Tk()
app.title("Weather app")
app.geometry('1250x600')
app.configure(bg='lightblue')

label_1 = Label(app, text='Instert city: ', font=('bold', 14), width = 16, bg='lightblue')
label_1.grid(row=0, column=0)

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text, font=('bold', 14), width = 16)
city_entry.grid(row=0, column=1)

search_btn = Button(app, text="Current weather", font=('bold', 14), width=16, command=search,bg='yellow')
search_btn.grid(row=1, column=0)

forecast_btn = Button(app, text="Weather Forecast", font=('bold', 14), width=16, command=forecast,bg='yellow')
forecast_btn.grid(row=1, column=1)

location_lbl = Label(app, text="", font=('bold ', 26), bg='lightblue')
location_lbl.grid(row=2, column=0)

img = PhotoImage(file='')
image = Label(app, image=img, bg='lightblue')
image.grid(row=4, column=0)

temp_lbl = Label(app, text='',font=('Calibri bold', 36), bg='lightblue')
temp_lbl.grid(row=3, column=0)

temp_lbl_0 = Label(app, text='',font=('bold', 34), bg='lightblue')
temp_lbl_0.grid(row=5, column=0)

temp_lbl_1 = Label(app, text='',font=('bold', 34), bg='lightblue')
temp_lbl_1.grid(row=5, column=1)

temp_lbl_2 = Label(app, text='',font=('bold', 34), bg='lightblue')
temp_lbl_2.grid(row=5, column=2)

temp_lbl_3 = Label(app, text='',font=('bold', 34), bg='lightblue')
temp_lbl_3.grid(row=5, column=3)

temp_lbl_4 = Label(app, text='',font=('bold', 34), bg='lightblue')
temp_lbl_4.grid(row=5, column=4)

temp_lbl_5 = Label(app, text='',font=('bold', 34), bg='lightblue')
temp_lbl_5.grid(row=5, column=5)

temp_lbl_6 = Label(app, text='',font=('bold', 34), bg='lightblue')
temp_lbl_6.grid(row=5, column=6)

weather_lbl = Label(app, text='',font=('bold', 16), bg='lightblue')
weather_lbl.grid(row=2, column=2)

weather_lbl_0 = Label(app, text='',font=('bold', 16), bg='lightblue')
weather_lbl_0.grid(row=7, column=0)

weather_lbl_1 = Label(app, text='',font=('bold', 16), bg='lightblue')
weather_lbl_1.grid(row=7, column=1)

weather_lbl_2 = Label(app, text='',font=('bold', 16), bg='lightblue')
weather_lbl_2.grid(row=7, column=2)

weather_lbl_3 = Label(app, text='',font=('bold', 16), bg='lightblue')
weather_lbl_3.grid(row=7, column=3)

weather_lbl_4 = Label(app, text='',font=('bold', 16), bg='lightblue')
weather_lbl_4.grid(row=7, column=4)

weather_lbl_5 = Label(app, text='',font=('bold', 16), bg='lightblue')
weather_lbl_5.grid(row=7, column=5)

weather_lbl_6 = Label(app, text='',font=('bold', 16), bg='lightblue')
weather_lbl_6.grid(row=7, column=6)

wind_speed_lbl = Label(app, text='', font=('bold', 16), bg='lightblue')
wind_speed_lbl.grid(row=3, column=2)

wind_speed_lbl_0 = Label(app, text='', font=('bold', 16), bg='lightblue')
wind_speed_lbl_0.grid(row=10, column=0)

wind_speed_lbl_1 = Label(app, text='', font=('bold', 16), bg='lightblue')
wind_speed_lbl_1.grid(row=10, column=1)

wind_speed_lbl_2 = Label(app, text='', font=('bold', 16), bg='lightblue')
wind_speed_lbl_2.grid(row=10, column=2)

wind_speed_lbl_3 = Label(app, text='', font=('bold', 16), bg='lightblue')
wind_speed_lbl_3.grid(row=10, column=3)

wind_speed_lbl_4 = Label(app, text='', font=('bold', 16), bg='lightblue')
wind_speed_lbl_4.grid(row=10, column=4)

wind_speed_lbl_5 = Label(app, text='', font=('bold', 16), bg='lightblue')
wind_speed_lbl_5.grid(row=10, column=5)

wind_speed_lbl_6 = Label(app, text='', font=('bold', 16), bg='lightblue')
wind_speed_lbl_6.grid(row=10, column=6)


app.mainloop()