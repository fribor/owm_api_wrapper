import requests
import pandas as pd
import time
import datetime as dtime

def get_weather_data(lat, lng, api_key, primary_key=None):
    
    app_id = api_key
    api_call = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&mode=json&units=metric'.format(lat, lng, app_id)

    dat = requests.post(api_call)
    dat = dat.json()
    data = {}
    if primary_key is not None:
        data['primary_key'] = primary_key
    data['time'] = dtime.datetime.fromtimestamp(int(dat['dt'])).strftime('%Y-%m-%d %H:%M:%S')
    data['week_id'] = dtime.datetime.fromtimestamp(int(dat['dt'])).strftime('%w%U%Y')
    data['weather'] = dat['weather'][0]['description']
    data['temp'] = dat['main']['temp']
    data['temp_min'] = dat['main']['temp_min']
    data['temp_max'] = dat['main']['temp_max']
    data['pressure'] = dat['main']['pressure']
    data['humidity'] = dat['main']['humidity']
    data['wind_spd'] = dat['wind']['speed']
    if 'deg' in dat['wind']:
        data['wind_deg'] = dat['wind']['deg']
    data['sunrise'] = dtime.datetime.fromtimestamp(int(dat['sys']['sunrise'])).strftime('%Y-%m-%d %H:%M:%S')
    data['sunset'] = dtime.datetime.fromtimestamp(int(dat['sys']['sunset'])).strftime('%Y-%m-%d %H:%M:%S')
    df = pd.DataFrame(data,index=[0])

    return df