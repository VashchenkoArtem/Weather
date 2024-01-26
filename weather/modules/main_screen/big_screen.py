import customtkinter
import requests
from PIL import Image
import requests
import modules.time as m_time
import modules.temp as m_temp
from datetime import datetime
import modules.main_screen.weather as m_weather
import modules.time as m_time
import modules.main_screen.weather_in_other_city as m_city
import modules.main_screen.temp_city as m_temp_city
import modules.main_screen.hours.time as m_after_hours
import modules.main_screen.hours.temp as m_after_temp
import modules.main_screen.hours.weather as m_after_weather
import modules.mini_screen.mini_screen as m_mini_screen
count = 0 
def big_screen(screen):
    screen.withdraw()
    def surch_weather():
        global count
        city = search.get()
        m_weather.update_weather(city, temp_lable,weather_label,sunrise_label,sunset_label,condition_label,big_screen)
        count = 1
        time_label.destroy()
        label_time = customtkinter.CTkLabel(master= big_screen,
                                    bg_color = "#5DA7B1",
                                    font= font,
                                    text_color= "white")
        label_time.place(x = 936, y = 191)
        m_time.update_time(label_time, f"http://worldtimeapi.org/api/timezone/Europe/{city}")
        return count

    #   screen.destroy()
    big_screen = customtkinter.CTkToplevel()
    # Додаємо до цього об'екта назву
    big_screen.title("Weather")
    big_screen.resizable(width= False, height= False)
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

    path_Kyiv = "images/Kyiv.png"
    image_Kyiv = customtkinter.CTkImage(Image.open(path_Kyiv), size = (233, 101))
    button_kyiv = customtkinter.CTkButton(master= big_screen,
                                          command= lambda: m_city.Kyiv(temp_label=temp_lable,
                                                                       time_label= time_label,
                                                                       screen= big_screen,
                                                                       city= "Kyiv"
                                                                       ),
                                          border_width= 2,
                                          corner_radius= 20,
                                          width = 236,
                                          height = 101,
                                          text = " ",
                                          border_spacing= 0,
                                          bg_color= "#096C82",
                                          fg_color="#096C82",
                                          border_color= "white",
                                          hover_color= "#096C82"
                                          )
    button_kyiv.place(x = 19, y = 164)
    button_Rome = customtkinter.CTkButton(master= big_screen,
                                          command= lambda: m_city.Kyiv(temp_label=temp_lable,
                                                                       time_label= time_label,
                                                                       screen= big_screen,
                                                                       city= "Rome"
                                                                       ),
                                          border_width= 2,
                                          corner_radius= 20,
                                          width = 236,
                                          height = 101,
                                          text = " ",
                                          border_spacing= 0,
                                          bg_color= "#096C82",
                                          fg_color="#096C82",
                                          border_color= "white",
                                          hover_color= "#096C82"
                                          )
    button_Rome.place(x = 19, y = 297)
    button_Dnipro = customtkinter.CTkButton(master= big_screen,
                                          # command= lambda: m_city.Kyiv(time_label= time_label,
                                          #                                temp_label= temp_lable,
                                          #                                screen= big_screen,
                                          #                                city= "Dnipro"
                                          #                              ),
                                          border_width= 2,
                                          corner_radius= 20,
                                          width = 236,
                                          height = 101,
                                          text = " ",
                                          border_spacing= 0,
                                          bg_color= "#096C82",
                                          fg_color="#096C82",
                                          border_color= "white",
                                          hover_color= "#096C82")
    button_Dnipro.place(x = 19, y = 31)
    button_London = customtkinter.CTkButton(master= big_screen,
                                          command= lambda: m_city.Kyiv(time_label= time_label,
                                                                         temp_label= temp_lable,
                                                                         screen= big_screen,
                                                                         city= "London"
                                                                       ),
                                          border_width= 2,
                                          corner_radius= 20,
                                          width = 236,
                                          height = 101,
                                          text = " ",
                                          border_spacing= 0,
                                          bg_color= "#096C82",
                                          fg_color="#096C82",
                                          border_color= "white",
                                          hover_color= "#096C82")
    button_London.place(x = 19, y = 430)
    button_Warsaw = customtkinter.CTkButton(master= big_screen,
                                          command= lambda: m_city.Kyiv(time_label= time_label,
                                                                         temp_label= temp_lable,
                                                                         screen= big_screen,
                                                                         city= "Warsaw"
                                                                       ),
                                          border_width= 2,
                                          corner_radius= 20,
                                          width = 236,
                                          height = 101,
                                          text = " ",
                                          border_spacing= 0,
                                          bg_color= "#096C82",
                                          fg_color="#096C82",
                                          border_color= "white",
                                          hover_color= "#096C82")
    button_Warsaw.place(x = 19, y = 563)
    button_Praque = customtkinter.CTkButton(master= big_screen,
                                          command= lambda: m_city.Kyiv(time_label= time_label,
                                                                         temp_label= temp_lable,
                                                                         screen= big_screen,
                                                                         city= "Prague"
                                                                       ),
                                          border_width= 2,
                                          corner_radius= 20,
                                          width = 236,
                                          height = 101,
                                          text = " ",
                                          border_spacing= 0,
                                          bg_color= "#096C82",
                                          fg_color="#096C82",
                                          border_color= "white",
                                          hover_color= "#096C82")
    button_Praque.place(x = 19, y = 696)
    name_Kyiv = customtkinter.CTkLabel(master= big_screen,
                                       text = "Kyiv",
                                       text_color="white",
                                       bg_color= "#096C82")
    name_Kyiv.place(x = 33, y = 172)
    name_Rome = customtkinter.CTkLabel(master= big_screen,
                                       text = "Rome",
                                       text_color="white",
                                       bg_color= "#096C82")
    name_Rome.place(x = 33, y = 305)
    name_London = customtkinter.CTkLabel(master= big_screen,
                                       text = "London",
                                       text_color="white",
                                       bg_color= "#096C82")
    name_London.place(x = 33, y = 443)
    name_Warsaw = customtkinter.CTkLabel(master= big_screen,
                                       text = "Warsaw",
                                       text_color="white",
                                       bg_color= "#096C82")
    name_Warsaw.place(x = 33, y = 576)
    name_Praque= customtkinter.CTkLabel(master= big_screen,
                                       text = "Prague",
                                       text_color="white",
                                       bg_color= "#096C82")
    name_Praque.place(x = 33, y = 709)
    name_Dnipro = customtkinter.CTkLabel(master= big_screen,
                                       text = "Dnipro",
                                       text_color="white",
                                       bg_color= "#096C82")
    name_Dnipro.place(x = 33, y = 40)
    time_Dnipro = customtkinter.CTkLabel(master= big_screen,
                                        bg_color="#096C82",
                                        font= font_time,
                                        text_color= "white")
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
                                    hover_color= "#096C82",
                                    )
    button.place(x = 1085, y = 38)
    weather_label = customtkinter.CTkLabel(big_screen, text = " ")
    sunrise_label = customtkinter.CTkLabel(big_screen, text = " ")
    sunset_label = customtkinter.CTkLabel(big_screen, text= ' ')
    condition_label = customtkinter.CTkLabel(big_screen, text=' ')
    # weather_label = customtkinter.CTkLabel(big_screen, text=" ", fg_color= "#5DA7B1", bg_color = "#5DA7B1", border_color ="#5DA7B1")
    # weather_label.place(x = 100, y = 100)
    m_weather.get_weather("Dnipro")
    time_Kyiv = customtkinter.CTkLabel(master= big_screen,
                                        bg_color= "#096C82",
                                        text_color= "white",
                                        font = font_time)
    time_Rome.place(x = 33, y = 330)
    time_Prague.place(x = 33, y = 729)
    time_Warsaw.place(x = 33, y = 596)
    time_London.place(x = 33, y = 463)
    time_Kyiv.place(x = 33, y = 197)
    # time_Dnipro.place(x = 33, y = 61)
    temp_lable.place(x = 683, y = 203)
    path_to_file = "images/avatar.png"
    # avatar = customtkinter.CTkImage(light_image= Image.open(path_to_file),size= (48,50))
    # avatar_button  = customtkinter.CTkButton(big_screen, width=48,height=50, image= avatar,text=" ",fg_color= "#5DA7B1", bg_color="#5DA7B1",hover_color="#5DA7B1",command= display_entries)
    # avatar_button.place(x= 318, y= 29)
    # Пример вызова функции
    m_weather.update_weather(city = "Dnipro", temp_lable=temp_lable, window1=big_screen, weather_label=weather_label, sunrise_lable = sunrise_label, sunset_ladel=sunset_label, condition_label=condition_label)

    m_time.only_time(time_Prague, "http://worldtimeapi.org/api/timezone/Europe/Prague")
    m_time.only_time(time_Warsaw, "http://worldtimeapi.org/api/timezone/Europe/Warsaw")
    m_time.only_time(time_Rome, "http://worldtimeapi.org/api/timezone/Europe/Rome")
    m_time.only_time(time_Kyiv, "http://worldtimeapi.org/api/timezone/Europe/Kyiv")
    m_time.only_time(time_London, "http://worldtimeapi.org/api/timezone/Europe/London")
    # m_time.only_time(time_Dnipro, "http://worldtimeapi.org/api/timezone/Europe/Dnipro")
    search.place(x = 918, y = 31)
    m_temp_city.temp_city(big_screen)
    # m_temp.temp("Dnipro",temp_lable, big_screen)
    if count == 0:
        m_time.update_time(time_label, "http://worldtimeapi.org/api/timezone/Europe/Kyiv")
    print("12121")
    m_after_hours.weather(city= "Dnipro", count= 0, x = 19 + 325, y = 484, screen= big_screen)
    weather_label1 = customtkinter.CTkLabel(master= big_screen,
                                            text = " ")
    m_after_hours.weather(city= "Dnipro", count= 1, x = 441, y = 484, screen= big_screen)
    m_after_hours.weather(city= "Dnipro", count= 2, x = 208 + 325, y = 484, screen= big_screen)
    m_after_hours.weather(city= "Dnipro", count= 3, x = 625, y = 484, screen= big_screen)
    m_after_hours.weather(city= "Dnipro", count= 4, x = 625 + 92, y = 484, screen= big_screen)
    m_after_hours.weather(city= "Dnipro", count= 5, x = 484 + 325, y = 484, screen= big_screen)
    m_after_hours.weather(city= "Dnipro", count= 6, x = 576 + 325, y = 484, screen= big_screen)
    m_after_hours.weather(city= "Dnipro", count= 7, x = 668 + 325, y = 484, screen= big_screen)
    m_after_hours.weather(city= "Dnipro", count= 8, x = 760 + 325, y = 484, screen= big_screen)
    temp_lable1 = customtkinter.CTkLabel(
                                         master= screen,
                                              font= ("Roboto Slab", 18),
                                              text_color = "white",
                                              bg_color = "#5DA7B1")
    temp_lable1.place(x = 445, y = 173 + 430)
    m_after_temp.get_temperature(city_name= "Dnipro",
                                 screen= big_screen,
                                 x = 120 + 325,
                                 y = 176 + 430,
                                 count= 1)
    m_after_temp.get_temperature(city_name= "Dnipro",
                                 screen= big_screen,
                                 x = 209 + 325,
                                 y = 176 + 430,
                                 count= 2)
    m_after_temp.get_temperature(city_name= "Dnipro",
                                 screen= big_screen,
                                 x = 310 + 325,
                                 y = 176 + 430,
                                 count= 3)
    m_after_temp.get_temperature(city_name= "Dnipro",
                                 screen= big_screen,
                                 x = 406 + 325,
                                 y = 176 + 430,
                                 count= 4)
    m_after_temp.get_temperature(city_name= "Dnipro",
                                 screen= big_screen,
                                 x = 498 + 325,
                                 y = 176 + 430,
                                 count= 5)
    m_after_temp.get_temperature(city_name= "Dnipro",
                                 screen= big_screen,
                                 x = 590 + 325,
                                 y = 176 + 430,
                                 count= 6)
    m_after_temp.get_temperature(city_name= "Dnipro",
                                 screen= big_screen,
                                 x = 682 + 325,
                                 y = 176 + 430,
                                 count= 7)
    m_after_temp.get_temperature(city_name= "Dnipro",
                                 screen= big_screen,
                                 x = 774 + 325,
                                 y = 176 + 430,
                                 count= 8)
    m_after_temp.get_temperature(city_name= "Dnipro",
                                 screen= big_screen,
                                 x = 26 + 325,
                                 y = 176 + 430,
                                 count= 0)
    mini_screen_button = customtkinter.CTkButton(master = big_screen, 
                                                 text = "Mini",
                                                 bg_color = "#5DA7B1",
                                                 fg_color="#5DA7B1",
                                                 command= lambda: m_mini_screen.mini_screen(screen= big_screen)
                                                 )
    m_after_weather.weather(city = "Dnipro",
                            window= big_screen,
                            x = 112 + 325,
                            y = 104 + 430,
                            count = 1,
                            width = 50,
                            height = 54,
                            label= weather_label1)
    m_after_weather.weather(city = "Dnipro",
                            window= big_screen,
                            x = 19 + 325,
                            y = 104 + 430,
                            count = 0,
                            width= 50,
                            height= 54, 
                            label = weather_label1)
    m_after_weather.weather(city = "Dnipro",
                            window= big_screen,
                            x = 204 + 325,
                            y = 104 + 430,
                            count = 2,
                            width = 50,
                            height= 54,
                            label = weather_label1)
    m_after_weather.weather(city = "Dnipro",
                            window= big_screen,
                            x = 296 + 325,
                            y = 104 + 430,
                            count = 3,
                            width = 50,
                            height= 54,
                            label = weather_label1)
    m_after_weather.weather(city = "Dnipro",
                            window= big_screen,
                            x = 388 + 325,
                            y = 104 + 430,
                            count = 4,
                            width = 50, 
                            height = 54,
                            label = weather_label1)
    m_after_weather.weather(city = "Dnipro",
                            window= big_screen,
                            x = 480 + 325,
                            y = 104 + 430,
                            count = 5,
                            width = 50,
                            height = 54,
                            label = weather_label1)
    m_after_weather.weather(city = "Dnipro",
                            window= big_screen,
                            x = 572 + 325,
                            y = 104 + 430,
                            count = 6,
                            width= 50,
                            height = 54,
                            label = weather_label1)
    m_after_weather.weather(city = "Dnipro",
                            window= big_screen,
                            x = 664 + 325,
                            y = 104 + 430,
                            count = 7,
                            width = 50,
                            height= 54,
                            label = weather_label1)
    m_after_weather.weather(city = "Dnipro",
                            window= big_screen,
                            x = 756 + 325,
                            y = 104 + 430,
                            count = 8,
                            width=50,
                            height = 54,
                            label = weather_label1)
    mini_screen_button.place(x = 576, y = 80)
    big_screen.mainloop()