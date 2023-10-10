#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

api_key = '9a96cf8d2b9ab455a412060b245f5750'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    visible = weather_data.json()['visibility']

    print("The weather in {user_input} is: {weather}")
    print("The temperature in {user_input} is: {temp}ºF")
     print("The weather in {user_input} is: {visible}")


# In[ ]:




