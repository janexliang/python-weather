from dotenv import load_dotenv
import os
from pprint import pprint
import requests

load_dotenv()

def get_current_weather(city="Ottawa", ):  ## assign Ottawa as default city
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    weather_data = requests.get(request_url).json()  ##  Send GET request to request_url to pull weather_data and cast to .json format

    ##pprint(weather_data)

    return weather_data

if __name__ == "__main__":
    
    city = input('\nPlease enter a City: \n')
    ### check if enter empty value for city
    ### strip() to remove empty whitespace string
    if not bool(city.strip()):
        city = "Ottawa"

    weather_data = get_current_weather(city)
    pprint(weather_data)








