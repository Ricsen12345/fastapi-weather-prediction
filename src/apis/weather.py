from fastapi import APIRouter, status, HTTPException
from src.prisma import prisma
from src.model.weather import storeWeather

router = APIRouter()

@router.get("/weather", status_code=status.HTTP_200_OK)
async def getWeather():
  weatherData = await prisma.weather.find_many()
  return { "data": weatherData }

@router.post("/weather", status_code=status.HTTP_201_CREATED)
async def postWeather(weather: storeWeather):
  print(weather)
  # weatherData = await prisma.weather.create(data={
  #   'temperature': 10,
  #   'humidity': 10,
  #   'raindrop': 'dry'
  # })

  return { "message": "Data added successfully" }
