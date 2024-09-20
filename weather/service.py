
from abc import ABC, abstractmethod

import requests


class WeatherService(ABC):
    @abstractmethod
    def get_weather(self, latitude: float, longitude: float) -> dict:
        pass

class WeatherAPIService(WeatherService):
    def __init__(self, api_key:str) -> None:
        super().api_key = api_key

    def get_weather(self, api_key:str, latitude: float, longitude: float) -> dict:
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={latitude},{longitude}&aqi=no"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
