# # 
#     import customtkinter
# from modules.reg_screen import*
# from PIL import Image
# data_display_window = customtkinter.CTk() 
# data_display_window.title("Data Display Window") 
# data_display_window.geometry("460x645") 
# def on_button_click():
#     print("sadasda")
# def display_entries(): 
#     global entry1_value, entry2_value, entry3_value, entry4_value 

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
#     data_display_window.mainloop()
    # exit = customtkinter.CTkButton(data_display_window,
    #                                width= 36, height= 13, bg_color="#5DA7B1",fg_color="#5DA7B1",border_color="#5DA7B1")
    # exit.place(x = 370, y= 26)

        # go_big_screen = customtkinter.CTkButton(master = data_display_window, width= 218, height= 146,bg_color="#5DA7B1",fg_color="#5DA7B1",border_color="#5DA7B1", command= on_button_click())
    # go_big_screen.place(x =119, y = 546)
# display_entries()
# def button_event():
#     print("button pressed")
# button = customtkinter.CTkButton(data_display_window, text="CTkButton", command=button_event)
# button.place(x = 119, y = 546)