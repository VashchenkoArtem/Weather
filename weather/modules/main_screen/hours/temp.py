import requests
import customtkinter
def get_temperature(city_name, screen, x, y, count):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid=6c7e78e9b205a70a787a85e68afbb688"
    response = requests.get(url)
    

    if response.status_code == 200:

        data = response.json()
        
        temperature_hour = data['list'][count]['main']['temp']
        temperature_hour = temperature_hour -273,15
        temperature_hour = int(temperature_hour[0])
        temp_label = customtkinter.CTkLabel(master= screen,
                                              text= f"{temperature_hour}°C",
                                              font= ("Roboto Slab", 18),
                                              text_color = "white",
                                              bg_color = "#5DA7B1"
                                            )
        temp_label.place(x = x, y = y)