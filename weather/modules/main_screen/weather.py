import customtkinter
import requests
from PIL import Image
from datetime import datetime
# def get_weather(city):
#     api_key = 'f6808e17116639c81b7ff38d254ff692'
    
#     base_url = "http://api.openweathermap.org/data/2.5/weather"
#     params = {
#         "q": city,
#         "apiid": api_key,
#         "units": "metric"

#     }
#     # try:
#     response = requests.get(base_url, params=params) 
#     data = response.json() 

#     temperature = data["main"]["temp"] 
#     temperature = int(temperature)
#     weather_description = data["weather"][0]["description"] 
#     weather_condition = data["weather"][0]["main"]
#     sunrise = data['sys']['sunrise']
#     sunset = data['sys']['sunset']
#     sunset_time = datetime.utcfromtimestamp(sunset).strftime('%Y-%m-%d %H:%M:%S')
#     sunrise_time = datetime.utcfromtimestamp(sunrise).strftime('%Y-%m-%d %H:%M:%S')
#     # except:
#     #     print ("error")
def get_weather(city): 
    api_key = "f6808e17116639c81b7ff38d254ff692"
    base_url = "http://api.openweathermap.org/data/2.5/weather"   
 
    params = { 
        "q": city, 
        "appid": api_key, 
        "units": "metric" 
    } 
 
    response = requests.get(base_url, params=params) 
    data = response.json() 

    temperature = data["main"]["temp"] 
    temperature = int(temperature) 
    weather_description = data["weather"][0]["description"] 
    weather_condition = data["weather"][0]["main"] 
    sunrise_timestamp = data["sys"]["sunrise"] 
    sunset_timestamp = data["sys"]["sunset"]
    sunset_time = datetime.utcfromtimestamp(sunset_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    sunrise_time = datetime.utcfromtimestamp(sunrise_timestamp).strftime('%Y-%m-%d %H:%M:%S')

    return temperature, weather_condition, weather_description, sunrise_time,sunset_time
def update_weather(city,temp_lable,window1, weather_label,sunrise_lable, sunset_ladel,condition_label):
    temperature, weather_discription, sunrise, sunset, weather_condition = get_weather(city)
    current_time = datetime.utcnow()
    api_key = "f6808e17116639c81b7ff38d254ff692"
    base_url = "http://api.openweathermap.org/data/2.5/weather"   
    print("12")
    params = { 
        "q": city, 
        "appid": api_key, 
        "units": "metric" 
    }
    response = requests.get(base_url, params=params) 
    data = response.json() 
    temperature = data["main"]["temp"] 
    temperature = int(temperature) 
    weather_discription = data["weather"][0]["description"] 
    weather_condition = data["weather"][0]["main"] 
    sunrise_timestamp = data["sys"]["sunrise"] 
    sunset_timestamp = data["sys"]["sunset"]
    sunset_time = datetime.utcfromtimestamp(sunset_timestamp)
    sunrise_time = datetime.utcfromtimestamp(sunrise_timestamp)
    if temperature is not None:
        temp_lable.configure(text = f"{temperature}°C")
    if sunrise_time <= current_time<= sunset_time:
        if weather_discription == "clear sky":
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/sun_2412787.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380, y = 171)
        if weather_discription== 'light rain':
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/rainy_2412747.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380, y = 171)
        if weather_discription == 'moderate rain':
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/rainy_2412747.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380 , y = 171)
        if weather_discription == 'moderate snow':
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/snowy_2412768.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380 , y = 171) 
        if weather_discription == "light snow":
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/snowy_2412768.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380, y = 171)
        if weather_discription== 'heavy rain':
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/rainy_2412747.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380, y = 171)
        if weather_discription == 'freezing rain':
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/drizzle_2412695.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380 , y = 171)
        if weather_discription == 'drizzle':
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/drizzle_2412695.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380 , y = 171) 
        if weather_discription == "overcast clouds" or weather_discription == "scattered clouds" or weather_discription == "few clouds":
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/sunny_2412798.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380 , y = 171)             
    else:
        if weather_discription == "clear sky":
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/moon_2412729.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380, y = 171)
        if weather_discription== 'light rain':
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/rain_2412733.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380, y = 171)
        if weather_discription == 'moderate rain':
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/rain_2412733.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380 , y = 171)
        if weather_discription == 'moderate snow':
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/snowy_2412767.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380 , y = 171) 
        if weather_discription == "light snow":
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/snowy_2412767.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380, y = 171)
        if weather_discription== 'heavy rain':
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/rain_2412733.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380, y = 171)
        if weather_discription == 'freezing rain':
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/drizzle_2412691.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380 , y = 171)
        if weather_discription == 'drizzle':
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/drizzle_2412691.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380 , y = 171) 
        if weather_discription == "overcast clouds" or weather_discription == "scattered clouds" or weather_discription == "few clouds":
            pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/moon_2412729.png"), size= (171, 159))
            label = customtkinter.CTkLabel(window1,text = " ",image = pictures,fg_color = "#5DA7B1")
            label.place(x = 380 , y = 171)
def future_weather(city):
    api_key = "f6808e17116639c81b7ff38d254ff692"
    base_url = "http://api.openweathermap.org/data/2.5/forecast"   
 
    params = { 
        "q": city, 
        "appid": api_key, 
        "units": "metric" 
    }
    # try:

    response = requests.get(base_url, params=params) 
    data = response.json() 
    temp_current = data["list"][0]["main"]["temp"]
    current_description = data["list"][0]["weather"][0]["description"][4]['main']['temp'] 
    hour_descriprion = data["list"][1]["weather"][0]["description"][3]['main']['temp'] 
    hour_time = datetime.utcfromtimestamp(data['list'][1]['dt'])
    hour_temp = data['list'][1]['main']['temp']
    hour_2_temp = data["list"][2]['main']['temp']
    return temp_current, current_description,hour_descriprion,hour_time, hour_temp, hour_2_temp    
