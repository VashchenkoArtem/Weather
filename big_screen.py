import customtkinter
import requests
from PIL import Image
import requests
import modules.time as m_time
import modules.temp as m_temp
from datetime import datetime
import modules.main_screen.weather as m_weather

def big_screen():
    def surch_weather():
        city = search.get()
        m_weather.update_weather(city, temp_lable,weather_label,sunrise_label,sunset_label,condition_label,big_screen)
    #   screen.destroy()
    big_screen = customtkinter.CTkToplevel()
    # Додаємо до цього об'екта назву
    big_screen.title("Weather")
    # big_screen.resizable(width= False, height= False)
    big_screen.geometry("1200x800")
    font_time = customtkinter.CTkFont("Roboto Slab", 12)
    font_temp = customtkinter.CTkFont("Inter", 80)
    
    font = customtkinter.CTkFont("Roboto Slab", 40)
    path_to_photo = 'Images/screen_big.jpg'
    image = customtkinter.CTkImage(dark_image= Image.open(path_to_photo),
                                    size= (1200,800))
    image_lable = customtkinter.CTkLabel(master= big_screen,
                                            image= image,
                                            text=' ')
    image_lable.pack()
    time_label = customtkinter.CTkLabel(master= big_screen,
                                    bg_color = "#5DA7B1",
                                    font= font,
                                    text_color= "white")
    time_label.place(x = 936, y = 191)
    temp_lable = customtkinter.CTkLabel(master= big_screen,
                                        bg_color= "#5DA7B1",
                                        text_color = "white",
                                        font = font_temp
                                        )
    time_Kyiv = customtkinter.CTkLabel(master= big_screen,
                                        bg_color= "#096C82",
                                        text_color= "white",
                                        font = font_time)
    time_Rome = customtkinter.CTkLabel(master= big_screen,
                                        bg_color="#096C82",
                                        font= font_time,
                                        text_color= "white")
    time_London = customtkinter.CTkLabel(master= big_screen,
                                        bg_color= "#096C82",
                                        font= font_time,
                                        text_color= "white")
    time_Warsaw = customtkinter.CTkLabel(master = big_screen,
                                        bg_color= "#096C82",
                                        font= font_time,
                                        text_color= "white")
    time_Prague = customtkinter.CTkLabel(master = big_screen,
                                        bg_color= "#096C82",
                                        font= font_time,
                                        text_color= "white")
    search = customtkinter.CTkEntry(master= big_screen,
                                    width = 218,
                                    height= 46,
                                    bg_color= "#5DA7B1",
                                    fg_color= "#096C82",
                                    border_color="white",
                                    border_width=5,
                                    corner_radius= 20,
                                    text_color= "white")
    image_search = customtkinter.CTkImage(light_image= Image.open("images/icon/search.png"), size = (20, 20))
    button = customtkinter.CTkButton(big_screen, 
                                    command = surch_weather,
                                    text = " ",
                                    corner_radius= 20,
                                    bg_color= '#096C82',
                                    image= image_search,
                                    width= 5,
                                    height= 5,
                                    fg_color= "#096C82",
                                    hover_color= "#096C82"
                                    )
    button.place(x = 1085, y = 38)
    weather_label = customtkinter.CTkLabel(big_screen, text = " ")
    sunrise_label = customtkinter.CTkLabel(big_screen, text = " ")
    sunset_label = customtkinter.CTkLabel(big_screen, text= ' ')
    condition_label = customtkinter.CTkLabel(big_screen, text=' ')
    # weather_label = customtkinter.CTkLabel(big_screen, text=" ", fg_color= "#5DA7B1", bg_color = "#5DA7B1", border_color ="#5DA7B1")
    # weather_label.place(x = 100, y = 100)
    m_weather.get_weather("Dnipro")
    time_Rome.place(x = 33, y = 330)
    time_Prague.place(x = 33, y = 729)
    time_Warsaw.place(x = 33, y = 596)
    time_London.place(x = 33, y = 463)
    time_Kyiv.place(x = 33, y = 197)
    temp_lable.place(x = 683, y = 203)
    path_to_file = "images/avatar.png"
    # avatar = customtkinter.CTkImage(light_image= Image.open(path_to_file),size= (48,50))
    # avatar_button  = customtkinter.CTkButton(big_screen, width=48,height=50, image= avatar,text=" ",fg_color= "#5DA7B1", bg_color="#5DA7B1",hover_color="#5DA7B1",command= display_entries)
    # avatar_button.place(x= 318, y= 29)
    m_weather.update_weather("Dnipro", temp_lable, weather_label,sunrise_label, sunset_label, condition_label, window = big_screen)
    m_time.only_time(time_Prague, "http://worldtimeapi.org/api/timezone/Europe/Prague")
    m_time.only_time(time_Warsaw, "http://worldtimeapi.org/api/timezone/Europe/Warsaw")
    m_time.only_time(time_Rome, "http://worldtimeapi.org/api/timezone/Europe/Rome")
    m_time.only_time(time_Kyiv, "http://worldtimeapi.org/api/timezone/Europe/Kyiv")
    m_time.only_time(time_London, "http://worldtimeapi.org/api/timezone/Europe/London")
    search.place(x = 918, y = 31)
    # m_temp.temp("Dnipro",temp_lable, big_screen)
    m_time.update_time(time_label, "http://worldtimeapi.org/api/timezone/Europe/Kyiv")
    print("12121")
    big_screen.mainloop()