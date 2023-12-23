import requests

def temp(city,label,screen):
    api_key = "f6808e17116639c81b7ff38d254ff692"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print("Error")
    
    temperature = data["main"]["temp"]
    temperature = int(temperature)
    screen.after(300000,lambda:temp(city,label,screen))
    label.configure(text = f"{temperature}°C")
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
        