import requests
import datetime

parameters = {
    "appid": "40900f94e736eb9228a515633523f376",
    "lat" : -17.783279,
    "lon" : -63.179161,
    "cnt": 4, 
}



response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)

response.raise_for_status()

weather_data = response.json()

forecast_list = weather_data['list']

# time_now = datetime.datetime.now().hour
# for x in range(20):
#     import random
#     xtime = random.randint(0, 23)
#     if time_now < xtime <time_now :
#         print(f' {xtime} In range')



for x in forecast_list:
    
    print(f'{x["weather"][0]["id"]}\n')
    


