import requests
import datetime
import customtkinter
import modules.time as m_time
def weather(city, screen, count,x, y):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=6c7e78e9b205a70a787a85e68afbb688"
    response = requests.get(url)
    ans = response.json()
    current_time = datetime.datetime.now()
    time_after_hours = current_time + datetime.timedelta(hours= count)
    formatted_time = time_after_hours.strftime('%H:%M')
    time_label_hours = customtkinter.CTkLabel(master= screen,
                                              text= formatted_time,
                                              font= ("Roboto Slab", 18),
                                              text_color = "white",
                                              bg_color = "#5DA7B1")
    time_label_hours.place(x = x, y = y)
    time_label_hours.after(100000,lambda:weather(city, screen, count, x, y))