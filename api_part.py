from create_file import create_csv
import requests
import os


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
    :return: The weather forecast info and put them into a csv file
    :rtype: tuple(str, str, float, str, float, str, float, str, float, str, float, str, float, str, float, str, float, float, float, float, float, float, float)
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