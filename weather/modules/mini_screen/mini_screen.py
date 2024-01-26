import customtkinter
from PIL import Image
import modules.temp as m_temp
import modules.main_screen.hours.weather as m_weather

path_mini = "images/Mini_screen.jpg"
path_to_update = "images/update.png"

def update(screen, temp_label):
    screen.after(300000,lambda:m_temp.temp(label = temp_label,
                                        screen= mini_screen)
                                        )
    screen.after(300000, lambda:m_weather.weather(m_weather.weather(city= "Dnipro",
                             window = mini_screen,
                             x = 17,
                             y = 18,
                             count = 0,
                             width= 179.54,
                             height = 142)))
def mini_screen(screen):
    screen.destroy()
    mini_screen = customtkinter.CTkToplevel()

    mini_screen.geometry("350x350")

    mini_screen.title("Mini Screen")

    bg_image = customtkinter.CTkImage(light_image= Image.open(path_mini), size = (350, 350))

    bg_label = customtkinter.CTkLabel(master= mini_screen,
                                      width = 350,
                                      height = 350,
                                      image= bg_image,
                                      text = " ")
    bg_label.place(x = 0, y = 0)

    temp_label = customtkinter.CTkLabel(master = mini_screen,
                                        bg_color = "#5DA7B1",
                                        text_color = "white",
                                        font= ("Inter", 80)
                                        )
    temp_label.place(x = 259, y = 199)

    weather_label = customtkinter.CTkLabel(master= mini_screen,
                                           bg_color= "#5DA7B1",
                                           text= " "
                                           )
    
    weather_label.place(x = 17, y = 18)

    m_weather.weather(city= "Dnipro",
                             window = mini_screen,
                             x = 17,
                             y = 18,
                             count = 0,
                             width= 179.54,
                             height = 142,
                             label= weather_label)

    m_temp.temp(label = temp_label,
                screen= mini_screen)
    update_photo = customtkinter.CTkImage(light_image= Image.open(path_to_update), size = (25, 25))
    update_button = customtkinter.CTkButton(master= mini_screen,
                                            text= " ",
                                            command= update(screen= mini_screen,
                                                            temp_label= temp_label),
                                            bg_color= "#5DA7B1",
                                            image= update_photo,
                                            fg_color= "#5DA7B1",
                                            hover_color="#5DA7B1",
                                            width= 25,
                                            height= 25)
    update_button.place(x = 290, y = 20)

    mini_screen.mainloop()
