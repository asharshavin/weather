from pydantic import BaseModel

class DeviceLocation(BaseModel):
    latitude: float
    longitude: float