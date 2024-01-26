import requests
from datetime import datetime
from PIL import Image
import customtkinter
def weather(city, window, x, y, count,width, height, label):

    current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=f6808e17116639c81b7ff38d254ff692"
    

    response = requests.get(current_weather_url)
    

    if response.status_code == 200:

        current_weather_data = response.json()

        sunrise_timestamp = current_weather_data['sys']['sunrise']
        sunset_timestamp = current_weather_data['sys']['sunset']

        current_time_timestamp = datetime.utcnow().timestamp()

        hourly_forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=f6808e17116639c81b7ff38d254ff692"


        forecast_response = requests.get(hourly_forecast_url)
        
        if forecast_response.status_code == 200:

            forecast_data = forecast_response.json()

            weather_discription = forecast_data['list'][count]['weather'][0]['description']
            print(weather_discription)
            if sunrise_timestamp < current_time_timestamp < sunset_timestamp:
                if weather_discription == "clear sky":
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/sun_2412787.png"), size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)
                if weather_discription== 'light rain':
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/rainy_2412747.png"), size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)
                if weather_discription == 'moderate rain':
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/rainy_2412747.png"),  size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x , y = y)
                if weather_discription == 'moderate snow':
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/snowy_2412768.png"),  size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x , y = y) 
                if weather_discription == "light snow":
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/snowy_2412768.png"), size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)
                if weather_discription== 'heavy rain':
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/rainy_2412747.png"), size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)
                if weather_discription == 'freezing rain':
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/drizzle_2412695.png"), size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)
                if weather_discription == 'drizzle':
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/drizzle_2412695.png"), size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y) 
                if weather_discription == "overcast clouds" or weather_discription == "broken clouds" or weather_discription == "scattered clouds" or weather_discription == "few clouds":
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/sunny_2412798.png"),  size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)       
            else:
                if weather_discription == "clear sky":
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/moon_2412729.png"), size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)
                if weather_discription== 'light rain':
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/rain_2412733.png"),  size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)
                if weather_discription == 'moderate rain':
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/rain_2412733.png"),  size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)
                if weather_discription == 'moderate snow':
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/snowy_2412767.png"), size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)
                if weather_discription == "light snow":
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/snowy_2412767.png"),  size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)
                if weather_discription== 'heavy rain':
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/rain_2412733.png"), size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)
                if weather_discription == 'freezing rain':
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/drizzle_2412691.png"),  size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)
                if weather_discription == 'drizzle':
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/drizzle_2412691.png"),  size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)
                if weather_discription == "overcast clouds" or weather_discription == "scattered clouds" or weather_discription == "few clouds" or weather_discription =="broken clouds":
                    pictures = customtkinter.CTkImage(light_image= Image.open("Images/icon/moon_2412729.png"),size= (width, height))
                    label = customtkinter.CTkLabel(window,text = " ",image = pictures,fg_color = "#5DA7B1")
                    label.place(x = x, y = y)


# import requests
# import customtkinter
# from datetime import datetime
# from PIL import Image

# def weather(city, window):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=f6808e17116639c81b7ff38d254ff692"
    
#     # Отправка запроса
#     response = requests.get(url)
    
#     # Проверка успешности запроса
#     if response.status_code == 200:
#         # Парсинг ответа
#         data = response.json()

#         # Извлечение времени восхода и захода солнца
#         sunrise_timestamp = data['sys']['sunrise']
#         sunset_timestamp = data['sys']['sunset']

#         # Получение текущего времени
#         current_time_timestamp = datetime.utcnow().timestamp()
#     hourly_forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=f6808e17116639c81b7ff38d254ff692"
#     weather_discription = hourly_forecast_url['list'][1]['weather'][0]['description']