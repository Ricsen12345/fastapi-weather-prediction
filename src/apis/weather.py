from fastapi import APIRouter, status, HTTPException
from src.model.weather import getWeather, storeWeather, predictionResponse

router = APIRouter()

@router.get("/weather", status_code=status.HTTP_200_OK)
async def root():
  return { "message": "weather API route" }

@router.post("/weather", status_code=status.HTTP_201_CREATED)
async def postWeather():
  return { "message": "Data added successfully" }
