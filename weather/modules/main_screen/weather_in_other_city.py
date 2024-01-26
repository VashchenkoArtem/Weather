import customtkinter
import modules.time as m_time
import modules.temp as m_temp
from PIL import Image
import requests
import modules.main_screen.hours.time as m_after_hours
import datetime
new_temp = None
new_time = None

def Kyiv(temp_label, time_label, screen, city):
    print(city)

    global new_temp, new_time
    temp_label.destroy()
    time_label.destroy()
    if new_time and new_temp != None:
        new_temp.destroy()
        new_time.destroy()
    font = customtkinter.CTkFont("Roboto Slab", 40)
    font_temp = customtkinter.CTkFont("Inter", 80)
    font_name = customtkinter.CTkFont("Roboto Slab", 22)
    name_city = customtkinter.CTkLabel(master= screen,
                                       bg_color = "#5DA7B1",
                                       width = 87,
                                       height = 30,
                                       text = f"{city}",
                                       text_color= "white",
                                       font= font_name
                                    )
    name_city.place(x = 689, y = 162)
    new_time = customtkinter.CTkLabel(master = screen, 
                                    bg_color = "#5DA7B1",
                                    font= font,
                                    text_color= "white")
    new_time.place(x = 936, y = 191)
    new_temp = customtkinter.CTkLabel(master = screen,
                                    bg_color = "#5DA7B1",
                                    text_color= "white",
                                    font= font_temp)
    new_temp.place(x = 683, y = 203)
    m_time.update_time(label= new_time,
                        url= f"http://worldtimeapi.org/api/timezone/Europe/{city}")
    m_temp.temp(city= f"{city}",
                label= new_temp,
                screen= screen)
