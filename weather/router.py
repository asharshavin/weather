from fastapi import Depends, FastAPI
from service import WeatherService, WeatherAPIService
import redis
from schemas import DeviceLocation
from deps import GetTemperature


app = FastAPI()

# redis_client = redis.StrictRedis()

API_KEY = 'f979bdf85da349be90495236241809'

def get_weather_service():
    weather_service = WeatherAPIService(api_key=API_KEY)
    return GetTemperature(weather_service=weather_service)

@app.post('/')
def get_temperature(device_location: DeviceLocation, get_weather: GetTemperature = Depends(get_weather_service)):
    res = get_weather(API_KEY, device_location.latitude, device_location.longitude)
    return {'res':res, 'temperature':res['current']['temp_c'], 'cache':True}

