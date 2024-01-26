import customtkinter
import modules.temp as m_temp
import requests

def temp_city(screen):
    # Kyiv
    Kyiv_label = customtkinter.CTkLabel(master= screen,
                                        width= 67,
                                        height= 42,
                                        font= ("Inter", 50),
                                        text_color= "white",
                                        bg_color = "#096C82")
    Kyiv_label.place(x = 177, y = 176)
    m_temp.temp_city(city= "Kyiv",
                label= Kyiv_label,
                screen= screen,
                x = 160,
                y = 176) 
    # Dnipro
    Dnipro_label = customtkinter.CTkLabel(master= screen,
                                        width= 67,
                                        height= 42,
                                        font= ("Inter", 50),
                                        text_color= "white",
                                        bg_color = "#096C82")
    Dnipro_label.place(x = 177, y = 43)
    m_temp.temp_city(city= "Dnipro",
                     label= Dnipro_label,
                     screen= screen,
                     x = 160,
                     y = 43)
    # Rome
    Rome_label = customtkinter.CTkLabel(master= screen,
                                        width= 67,
                                        height= 42,
                                        font= ("Inter", 50),
                                        text_color= "white",
                                        bg_color = "#096C82")
    Rome_label.place(x = 177, y = 309)
    m_temp.temp_city(city= "Rome",
                     label= Rome_label,
                     screen= screen,
                     x = 160,
                     y = 309)
    # London
    London_label = customtkinter.CTkLabel(master= screen,
                                        width= 67,
                                        height= 42,
                                        font= ("Inter", 50),
                                        text_color= "white",
                                        bg_color = "#096C82")
    London_label.place(x = 177, y = 442)
    m_temp.temp_city(city= "London",
                     label= London_label,
                     screen= screen,
                     x = 160,
                     y = 442)
    # Warsaw
    Warsaw_label = customtkinter.CTkLabel(master= screen,
                                        width= 67,
                                        height= 42,
                                        font= ("Inter", 50),
                                        text_color= "white",
                                        bg_color = "#096C82")
    Warsaw_label.place(x = 177, y = 575)
    m_temp.temp_city(city= "Warsaw",
                     label= Warsaw_label,
                     screen= screen,
                     x = 160,
                     y  = 575)
    # Prague
    Prague_label = customtkinter.CTkLabel(master= screen,
                                        width= 67,
                                        height= 42,
                                        font= ("Inter", 50),
                                        text_color= "white",
                                        bg_color = "#096C82")
    Prague_label.place(x = 177, y = 708)
    m_temp.temp_city("Prague",
                     label= Prague_label,
                     screen= screen,
                     x = 160,
                     y = 708)