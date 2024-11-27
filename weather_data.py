import json
from importlib.resources import files

import requests

CITY_NAME = "Palanpur2"
API_END_POINT = f"https://wgoweather.herokuapp.com/weather/{CITY_NAME}"


class WeatherApiClient(object):


    def get_city_weather(self, city_name=""):
        try_limit = 1
        while try_limit < 3:
            try:
                print("called erer")
                API_END_POINT = f"https://goweather.herokuapp.com/weather/{city_name}"
                response = requests.get(API_END_POINT)
                print(response, "--")
                if response.status_code == 200:
                    json_res = response.json()
                    print(json_res, "--")
                    return {
                        "city" : city_name,
                        "temperature": json_res.get("temperature"),
                        "humidity": json_res.get("wind")
                    }
                try_limit += 1
            except Exception as e:
                try_limit += 1

        return {
                    "city" : city_name,
                    "temperature": "Unable to fetch",
                    "humidity": "Unable to fetch",
                }

    def get_weather_data_from_cities(self, city_list="Palanpur,Ahmedabad"):
        final_json = []
        for city in city_list.split(","):
            final_json.append(self.get_city_weather(city))
        return final_json

    def store_in_json(self, data, json_file_name="weather.json"):
        with open(json_file_name, 'w') as json_file:
            json.dump(data, json_file)

obj = WeatherApiClient()
json_data = obj.get_weather_data_from_cities()
obj.store_in_json(json_data)
