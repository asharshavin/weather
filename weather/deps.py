from weather.service import WeatherService
from schemas import DeviceLocation


class GetTemperature:
    def __init__(self, weather_service: WeatherService):
        self.weather_service = weather_service
    
    def execute(self, device_location: DeviceLocation) -> dict:
        latitude = device_location.latitude
        longitude = device_location.longitude

        weather_data = self.weather_service.get_weather(latitude, longitude)
        
        return weather_data
        
