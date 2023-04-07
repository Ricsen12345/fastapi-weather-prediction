from pydantic import BaseModel

class storeWeather(BaseModel):
  temperature: float
  humidity: float
  raindrop: str

class predictWeather(BaseModel):
  temperature: float
  humidity: float