from fastapi import FastAPI
from weather.schemas import DeviceLocation
import requests


app = FastAPI()

API_KEY = 'f979bdf85da349be90495236241809'

def get_weather(api_key, latitude: float, longitude: float) -> dict:
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={latitude},{longitude}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

@app.post('/')
def get_temperature(device_location: DeviceLocation):
    res = get_weather(API_KEY, device_location.latitude, device_location.longitude)
    return {'res':res, 'temperature':res['current']['temp_c'], 'cache':True}
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)