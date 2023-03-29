from fastapi import APIRouter

from src.apis.weather import router as weatherRouter

apis = APIRouter()
apis.include_router(weatherRouter)

__all__ = ["apis"]