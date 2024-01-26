import customtkinter
import sqlite3
from PIL import Image
import modules.main_screen.big_screen as m_big
import modules.time as m_time
import modules.temp as m_temp
import modules.main_screen.big_screen as m_big

entry1_value = ""
entry2_value = ""
entry3_value = ""
entry4_value = ""
count = 0


def save_to_database(entry1, entry2, entry3, entry4):

    global entry1_value, entry2_value, entry3_value, entry4_value
    entry1_value = entry1.get() 
    entry2_value = entry2.get() 
    entry3_value = entry3.get() 
    entry4_value = entry4.get() 
    # try:
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTOINCREMENT, text1 TEXT, text2 TEXT, text3 TEXT, text4 TEXT)')

    cursor.execute('INSERT INTO entries (text1, text2, text3, text4) VALUES (?, ?, ?, ?)',
                   (entry1.get(), entry2.get(), entry3.get(), entry4.get()))
    conn.commit()
    conn.close()
    print("Data saved to the database.")
    

    display_entries()

    # except Exception as e:
        # print(f"Error saving to the database: {e}")

def display_entries():
    # m_big.big_screen()
    def open_input_window():
        data_display_window.withdraw()
        input_window = customtkinter.CTkToplevel()
        input_window.title("Sign in")
        input_window.geometry("460x645")
        path_to_photo1 = "images/register_copy.png"
        back_image = customtkinter.CTkImage(light_image= Image.open(path_to_photo1), size = (465, 645))
        back = customtkinter.CTkLabel(input_window, width = 465,image= back_image, height= 645, text= " ", bg_color = "#5DA7B1", fg_color= "#5DA7B1")
        
        back.pack()

        entry1 = customtkinter.CTkEntry(input_window,width=218, height=46, bg_color = "#5DA7B1", fg_color= "#5DA7B1", corner_radius= 20, border_color= "white", border_width= 3, text_color="white")
        entry1.place(x=38, y=150)


        entry2 = customtkinter.CTkEntry(input_window, width=218, height=46, bg_color = "#5DA7B1", fg_color= "#5DA7B1", corner_radius= 20, border_color= "white", border_width= 3, text_color= "white")
        entry2.place(x=38, y=249)


        entry3 = customtkinter.CTkEntry(input_window,  width=295, height=46, bg_color = "#5DA7B1", fg_color= "#5DA7B1", corner_radius= 20, border_color= "white", border_width= 3, text_color="white",)
        entry3.place(x=38, y=348)


        entry4 = customtkinter.CTkEntry(input_window, width=295, height=46, bg_color = "#5DA7B1", fg_color= "#5DA7B1", corner_radius= 20, border_color= "white", border_width= 3, text_color="white")
        entry4.place(x=38, y=447)


        submit_button = customtkinter.CTkButton(input_window, text="Зберегти", command=lambda: on_button_click(entry1, entry2, entry3, entry4, input_window), bg_color='#5DA7B1', fg_color="#5DA7B1", corner_radius= 20, border_width= 3, width= 218, height = 46, border_color="white")
        submit_button.place(x=119, y=546)
        input_window.mainloop()

    global count
    global entry1_value, entry2_value, entry3_value, entry4_value
    data_display_window = customtkinter.CTkToplevel()
    font =customtkinter.CTkFont("Roboto Slab", 28, underline= True)
    data_display_window.title("Cabinet")
    data_display_window.geometry("460x645")
    path_to_cabinet = "images/cabinet.png"
    back_image = customtkinter.CTkImage(light_image= Image.open(path_to_cabinet), size = (465, 645))
    back = customtkinter.CTkLabel(data_display_window,image= back_image, text= " ", bg_color = "#5DA7B1", fg_color= "#5DA7B1")
    
    back.pack() 

    display_text_1 = entry1_value
    label_1 = customtkinter.CTkLabel(data_display_window, text=display_text_1, bg_color = "#5DA7B1", fg_color= '#5DA7B1', font = font, text_color = "white")
    label_1.place(x=119, y=157)


    display_text_2 = entry2_value
    label_2 = customtkinter.CTkLabel(data_display_window, text=display_text_2, bg_color = "#5DA7B1", fg_color= '#5DA7B1', font = font, text_color = "white")
    label_2.place(x=121, y=256)


    display_text_3 = entry3_value
    label_3 = customtkinter.CTkLabel(data_display_window, text=display_text_3, bg_color = "#5DA7B1", fg_color= '#5DA7B1', font = font, text_color = "white")
    label_3.place(x=119, y=352)


    display_text_4 = entry4_value
    label_4 = customtkinter.CTkLabel(data_display_window, text=display_text_4, bg_color = "#5DA7B1", fg_color= '#5DA7B1', font = font, text_color = "white")
    label_4.place(x=119, y=455) 

    # save_button = customtkinter.CTkButton(data_display_window, text="Save to Database", command=lambda: save_to_database(entry1, entry2, entry3, entry4))
    # save_button.place(x=200, y=500)  # Измените координаты в соответствии с вашими требованиями


    open_input_window_button = customtkinter.CTkButton(data_display_window, text="Перейти до додатку", command=lambda:m_big.big_screen(data_display_window), bg_color = "#5DA7B1", fg_color= "#096C82", text_color= "white", width = 218, height = 46, border_width= 5, border_color="white", corner_radius= 20)
    open_input_window_button.place(x=119, y=546) 
    exit = customtkinter.CTkButton(master = data_display_window, text="Вихід",bg_color="#5DA7B1", fg_color="#5DA7B1", text_color="white",command= data_display_window.destroy, width= 36, height= 13,border_width= 0,border_color= "white",corner_radius=20, hover_color="#5DA7B1")
    exit.place(x = 370, y = 26)
    return data_display_window


def on_button_click(entry1, entry2, entry3, entry4, screen):
    save_to_database(entry1, entry2, entry3, entry4)
    screen.withdraw()


path_to_photo = "images/reg_screen.png"
root = customtkinter.CTk()
root.title("Sign in")
root.geometry("460x645")
bg_cabinet = customtkinter.CTkImage(light_image=Image.open(path_to_photo),
                                size=(460, 645))
image_label = customtkinter.CTkLabel(root, image=bg_cabinet, text="")  # display image with a CTkLabel
# bg_label = customtkinter.CTkLabel(data_display_window, 460, 645, text= " ", image= bg_cabinet)
image_label.grid()
entry1 = customtkinter.CTkEntry(root,width=218, height=46, bg_color = "#5DA7B1", fg_color= "#5DA7B1", corner_radius= 20, border_color= "white", border_width= 3, text_color="white")
entry1.place(x=38, y=150)


entry2 = customtkinter.CTkEntry(root, width=218, height=46, bg_color = "#5DA7B1", fg_color= "#5DA7B1", corner_radius= 20, border_color= "white", border_width= 3, text_color= "white")
entry2.place(x=38, y=249)

entry3 = customtkinter.CTkEntry(root,  width=295, height=46, bg_color = "#5DA7B1", fg_color= "#5DA7B1", corner_radius= 20, border_color= "white", border_width= 3, text_color="white",)
entry3.place(x=38, y=348)


entry4 = customtkinter.CTkEntry(root, width=295, height=46, bg_color = "#5DA7B1", fg_color= "#5DA7B1", corner_radius= 20, border_color= "white", border_width= 3, text_color="white")
entry4.place(x=38, y=447)

submit_button = customtkinter.CTkButton(root, text="Зберегти", command=lambda: on_button_click(entry1, entry2, entry3, entry4, root), bg_color='#5DA7B1', fg_color="#5DA7B1", corner_radius= 20, border_width= 3, width= 218, height = 46, border_color="white")
submit_button.place(x=119, y=546)
font = customtkinter.CTkFont("Roboto Slab", 28)
button = customtkinter.CTkButton(root, text = "Реєстрація користувача", text_color = "white",fg_color = "#5DA7B1", bg_color = "#5DA7B1", hover_color= "#5DA7B1", font = font)
button.place(x=42, y = 38)
root.mainloop()



# import customtkinter  
# import sqlite3 
# from PIL import Image 
# import modules.temp as m_temp
# import modules.time as m_time
# import modules.weather as m_weather
# # Глобальные переменные для хранения значений Entry 
# entry1_value = "" 
# entry2_value = "" 
# entry3_value = "" 
# entry4_value = "" 


# def save(entry1, entry2, entry3, entry4): 
#     global entry1_value, entry2_value, entry3_value, entry4_value 
#     entry1_value = entry1.get()  # Сохраняем значение первой Entry 
#     entry2_value = entry2.get()  # Сохраняем значение второй Entry 
#     entry3_value = entry3.get()  # Сохраняем значение третьей Entry 
#     entry4_value = entry4.get()  # Сохраняем значение четвертой Entry 
#     # try: 
#     conn = sqlite3.connect('mydatabase.db') 
#     cursor = conn.cursor() 

#     # Создание таблицы, если её нет 
#     cursor.execute('CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTOINCREMENT, text1 TEXT, text2 TEXT, text3 TEXT, text4 TEXT)') 

#     # Вставка данных из Entry в таблицу 
#     cursor.execute('INSERT INTO entries (text1, text2, text3, text4) VALUES (?, ?, ?, ?)', 
#                    (entry1.get(), entry2.get(), entry3.get(), entry4.get())) 

#     conn.commit() 
#     conn.close() 
#     print("Data saved to the database.") 
#     display_entries()
#     # reg_screen.withdraw()
#     # ecept Exception as e: 
#     # print(f"Error saving to the database: {e}")


# def display_entries(): 
    
#     def big_screen():
#         data_display_window.withdraw()
#         big_screen = customtkinter.CTkToplevel()
#         big_screen.title("Weather Forecast")
#         big_screen.geometry("1200x800")

#         city_font = customtkinter.CTkFont("Roboto Slab", 12)
#         temp_font = customtkinter.CTkFont("Inter", 80)
#         font = customtkinter.CTkFont("Roboto Slab", 30)
#         path_to_photo = 'Images/screen_big.jpg'
#         image = customtkinter.CTkImage(dark_image= Image.open(path_to_photo),
#                                     size= (1200,800))
#         image_lable = customtkinter.CTkLabel(master= big_screen,
#                                             image= image,
#                                             text=' ',)
#         image_lable.pack()
#         font_avatar = customtkinter.CTkFont("Roboto Slab", 14)
#         avat  = customtkinter.CTkButton(big_screen, width=150,height=50,text=entry3_value,fg_color= "#5DA7B1", bg_color="#5DA7B1",hover_color="#5DA7B1", font = font_avatar)
#         avat.place(x = 350, y = 29)
#         time_label = customtkinter.CTkLabel(big_screen,
#                                             bg_color= "#5DA7B1",
#                                             font= font,
#                                             text_color= "white")
#         time_label.place(x = 936, y = 191)

#         temp_lable = customtkinter.CTkLabel(big_screen,
#                                             bg_color= "#5DA7B1",
#                                             font= temp_font,
#                                             text_color= "white")
#         temp_lable.place(x = 684, y = 203)

#         temp_lable_Kyiv = customtkinter.CTkLabel(big_screen,
#                                             bg_color= "#096C82",
#                                             font= city_font,
#                                             text_color= "white")
#         temp_lable_Kyiv.place(x = 33, y = 197)

#         temp_lable_Rome = customtkinter.CTkLabel(big_screen,
#                                             bg_color= "#096C82",
#                                             font= city_font,
#                                             text_color= "white")
#         temp_lable_Rome.place(x = 33, y = 330)

#         temp_lable_London = customtkinter.CTkLabel(big_screen,
#                                             bg_color= "#096C82",
#                                             font= city_font,
#                                             text_color= "white")
#         temp_lable_London.place(x = 33, y = 463)

#         temp_lable_Prague = customtkinter.CTkLabel(big_screen,
#                                             bg_color= "#096C82",
#                                             font= city_font,
#                                             text_color= "white")
#         temp_lable_Prague.place(x = 33, y = 729)
#         temp_lable_Warsaw = customtkinter.CTkLabel(big_screen,
#                                             bg_color= "#096C82",
#                                             font= city_font,
#                                             text_color= "white")
#         temp_lable_Warsaw.place(x = 33, y = 596)
#         button_search = customtkinter.CTkEntry(master= big_screen,
#                                                 width= 218,
#                                                 height= 46,
#                                                 bg_color= "#5DA7B1",
#                                                 fg_color="#096C82",
#                                                 border_color="white",
#                                                 border_width= 3, 
#                                                 corner_radius= 20,
#                                                 text_color= "white")
#         button_search.place(x= 918, y = 31)
#         weather_label = customtkinter.CTkLabel(big_screen, text = " ", fg_color ="#5DA7B1", bg_color ="#5DA7B1")
#         # weather_label.place(x= 100, y= 100)
#         m_weather.get_weather("Dnipro", weather_label, big_screen)
#         path_to_file = "images/avatar.png"
#         avatar = customtkinter.CTkImage(light_image= Image.open(path_to_file),size= (48,50))
#         avatar_button  = customtkinter.CTkButton(big_screen, width=48,height=50, image= avatar,text=" ",fg_color= "#5DA7B1", bg_color="#5DA7B1",hover_color="#5DA7B1",command= display_entries)
#         avatar_button.place(x= 318, y= 29)
#         big_screen.resizable(width = False, height = False)
#         m_temp.temp("Dnipro",temp_lable,big_screen)
#         m_time.only_time(temp_lable_Prague,("http://worldtimeapi.org/api/timezone/Europe/Prague"))
#         m_time.only_time(temp_lable_London,("http://worldtimeapi.org/api/timezone/Europe/London"))
#         m_time.only_time(temp_lable_Rome,("http://worldtimeapi.org/api/timezone/Europe/Rome"))
#         m_time.only_time(temp_lable_Kyiv, ("http://worldtimeapi.org/api/timezone/Europe/Kyiv"))
#         m_time.update_time(time_label, ("http://worldtimeapi.org/api/timezone/Europe/Kyiv"))
#         m_time.only_time(temp_lable_Warsaw,("http://worldtimeapi.org/api/timezone/Europe/warsaw"))
#         big_screen.mainloop()
#     global entry1_value, entry2_value, entry3_value, entry4_value 
#     data_display_window = customtkinter.CTkToplevel()   
#     data_display_window.title("Data Display Window") 
#     data_display_window.geometry("460x645") 

#     path_to_cabinet = "images/cabinet.png" 
#     bg_cabinet = customtkinter.CTkImage(light_image= Image.open(path_to_cabinet), size= (460, 645)) 
#     bg_label = customtkinter.CTkLabel(data_display_window, 460, 645, text= " ", image= bg_cabinet) 
#     bg_label.pack()
#     font1 = customtkinter.CTkFont('Roboto Slab', 28, underline= True)
#     text1 = entry1_value
#     text1_label = customtkinter.CTkLabel(data_display_window,
#                                         text= text1,bg_color="#5DA7B1", fg_color="#5DA7B1", text_color="white", font= font1)
#     text1_label.place(x =119, y = 157 )
#     text2 = entry2_value
#     text2_label = customtkinter.CTkLabel(data_display_window,
#                                         text= text2,bg_color="#5DA7B1", fg_color="#5DA7B1", text_color="white", font= font1)
#     text2_label.place(x =121, y = 256 )
#     text3 = entry3_value
#     text3_label = customtkinter.CTkLabel(data_display_window,
#                                         text= text3,bg_color="#5DA7B1", fg_color="#5DA7B1", text_color="white", font= font1)
#     text3_label.place(x =121, y = 352 )
#     text4 = entry4_value
#     text4_label = customtkinter.CTkLabel(data_display_window,
#                                         text= text4,bg_color="#5DA7B1", fg_color="#5DA7B1", text_color="white", font= font1)
#     text4_label.place(x =121, y = 455 )

#     
#     to_big_screen = customtkinter.CTkButton(master = data_display_window, text="Перейти до додатку",bg_color="#5DA7B1", fg_color="#096C82", text_color="white",command= big_screen, width= 218, height= 46,border_width= 5,border_color= "white",corner_radius=20)
#     to_big_screen.place(x= 119, y= 546)
#     data_display_window.mainloop()
#     return data_display_window

# def on_button_click(entry1, entry2, entry3, entry4, screen):
#     save(entry1, entry2, entry3, entry4)
#     root.withdraw()
# path_to_photo = "images/reg_screen.png"
# root = customtkinter.CTk()
# root.title("Data Entry Window")
# root.geometry("460x645")
# bg_cabinet = customtkinter.CTkImage(light_image=Image.open(path_to_photo),
#                                 size=(460, 645))
# image_label = customtkinter.CTkLabel(root, image=bg_cabinet, text="")  # display image with a CTkLabel
# # bg_label = customtkinter.CTkLabel(data_display_window, 460, 645, text= " ", image= bg_cabinet)
# image_label.grid()
# entry1 = customtkinter.CTkEntry(root,width=218, height=46, bg_color = "#5DA7B1", fg_color= "#5DA7B1", corner_radius= 20, border_color= "white", border_width= 3, text_color="white")
# entry1.place(x=38, y=150)

# # Создание и размещение второй Entry
# entry2 = customtkinter.CTkEntry(root, width=218, height=46, bg_color = "#5DA7B1", fg_color= "#5DA7B1", corner_radius= 20, border_color= "white", border_width= 3, text_color= "white")
# entry2.place(x=38, y=249)

# # Создание третьей Entry
# entry3 = customtkinter.CTkEntry(root,  width=295, height=46, bg_color = "#5DA7B1", fg_color= "#5DA7B1", corner_radius= 20, border_color= "white", border_width= 3, text_color="white",)
# entry3.place(x=38, y=348)

# # Создание четвертой Entry
# entry4 = customtkinter.CTkEntry(root, width=295, height=46, bg_color = "#5DA7B1", fg_color= "#5DA7B1", corner_radius= 20, border_color= "white", border_width= 3, text_color="white")
# entry4.place(x=38, y=447)

# # Создание кнопки "Submit"
# submit_button = customtkinter.CTkButton(root, text="Зберегти", command=lambda: on_button_click(entry1, entry2, entry3, entry4, root), bg_color='#5DA7B1', fg_color="#5DA7B1", corner_radius= 20, border_width= 3, width= 218, height = 46, border_color="white")
# submit_button.place(x=119, y=546)
# root.mainloop()