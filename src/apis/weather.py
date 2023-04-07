from fastapi import APIRouter, status
from src.prisma import prisma
from src.model.weather import storeWeather, predictWeather

import joblib
import numpy as np
from tensorflow import keras
from datetime import datetime

router = APIRouter()

@router.get("/weather", status_code=status.HTTP_200_OK)
async def getWeather():
  weatherData = await prisma.weather.find_many()
  return { "data": weatherData }

@router.post("/weather", status_code=status.HTTP_201_CREATED)
async def postWeather(weather: storeWeather):
  weatherData = await prisma.weather.create(data={'temperature': weather.temperature,
                                                  'humidity': weather.humidity,
                                                  'raindrop': weather.raindrop})
  return {"data": weatherData}

@router.post("/weather/predict", status_code=status.HTTP_200_OK)
def predictWeather(weather: predictWeather):
  loadedScaler = joblib.load('scaler.pkl')
  loadedModel = keras.models.load_model('deeplearning.h5')

  now = datetime.now()
  hour = round(now.hour + now.minute/60)

  weatherData = [[hour, weather.temperature, weather.humidity]]
  weatherDataScaled = loadedScaler.transform(weatherData)

  probability = loadedModel.predict(weatherDataScaled)
  result = np.argmax(probability) # type => np.int64
  result = np.int64(result).item() # type => python's int

  return {"message": result,
          "data": {"hour": hour,
                   "temperature": weather.temperature,
                   "humidity": weather.humidity}}