from pydantic import BaseModel

class getWeather:
  id: int
  temperature: float
  humidity: float
  raindrop: str
  class Config:
    orm_mode = True

class storeWeather:
  temperature: float
  humidity: float
  raindrop: str

class predictionResponse:
  prediction: str
  class Config:
    orm_mode = True