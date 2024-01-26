import requests
import customtkinter
def temp(label,screen,city ="Dnipro"):
    api_key = "f6808e17116639c81b7ff38d254ff692"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print("Error")
    
    temperature = data["main"]["temp"]
    temperature = int(temperature)
    screen.after(300000,lambda:temp(city,label,screen))
    label.configure(text = f"{temperature}°")
def temp_city(city,label,screen, x, y):
    api_key = "f6808e17116639c81b7ff38d254ff692"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print("Error")
    
    temperature = data["main"]["temp"]
    temperature = int(temperature)
    temperature_str = str(temperature)
    if len(temperature_str) > 2:
        label.destroy()
        label_1 = customtkinter.CTkLabel(master= screen,
                                        width= 67,
                                        height= 42,
                                        font= ("Inter", 50),
                                        text_color= "white",
                                        bg_color = "#096C82")
        label_1.place(x = x, y = y)

    screen.after(300000,lambda:temp(city,label,screen))
    if len(temperature_str) > 2:

        label_1.configure(text = f"{temperature}°")
    else:
        label.configure(text = f"{temperature}°")
# def temp(city,label,screen):
#     api_key = "f6808e17116639c81b7ff38d254ff692"

#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
#     response = requests.get(url)
#     data = response.json()

#     if response.status_code != 200:
#         print("Error")
    
#     temperature = data["main"]["temp"]
#     temperature = int(temperature)
#     screen.after(300000,lambda:temp(city,label,screen))
#     label.configure(text = f"{temperature}°")

# def temp_city(city,label,screen):
#     api_key = "f6808e17116639c81b7ff38d254ff692"

#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
#     response = requests.get(url)
#     data = response.json()

#     if response.status_code != 200:
#         print("Error")
    
#     temperature = data["main"]["temp"]
#     temperature = int(temperature)
#     temperature_str = str(temperature)
#     # if len(temperature_str) > 2:
#     #     print(temperature)
#     screen.after(300000,lambda:temp(city,label,screen))
#     label.configure(text = f"{temperature}°")
#     return temperature_str
# def get_current_temp():
#     try:
#         respons= requests.get("https://wttr.in/?format=%t")
#         temp = respons.text.strip()
#         return f"{temp}"
#     except:
#         return "Error"
    
# def update_current_temp(lable):
#     try:
#         current_temp = get_current_temp()
#         lable.configure(text = f"{current_temp}")
#         lable.after(1000, lambda: update_current_temp(lable))
#     except:
#         lable.configure(text = "Error")
#         lable.after(1000, lambda: update_current_temp(lable))
        