import requests

from datetime import datetime
def get_time(url):
    try:
        response = requests.get(url)

        data = response.json()
        current_time = data['datetime']
        return current_time
    except:
        return print(f'Error')


def update_time(label, url):
    # try:
        dt_object = get_time(url)

        time_object = datetime.strptime(dt_object, "%Y-%m-%dT%H:%M:%S.%f%z")
        time = time_object.strftime("%A \n %B %d\n %H:%M")
        label.configure(text= f'{time}')
        label.after(1000, lambda: update_time(label, url))
    # except Exception as e:
        # label.configure(text = f"Error {e}")
        # label.after(1000, lambda: update_time(label, url))

def only_time(label,url):
    # try:
    response = requests.get(url)
    data = response.json()
    current_time = data['datetime']
    time_object = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%S.%f%z")
    formatted_time = time_object.strftime("%H:%M")
    label.configure(text = f"{formatted_time}")
    label.after(1000,lambda:only_time(label,url))
    # except:
    #     label.configure(text = "Error")
    #     label.after(1000,lambda:only_time(label,url))
