# uvicorn main:app --reload
from fastapi import FastAPI, status
from fastapi.middleware.gzip import GZipMiddleware
from deta import Deta

from src.apis import apis
from src.prisma import prisma

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(apis, prefix="/apis")

@app.get("/", status_code=status.HTTP_200_OK)
def root():
  return { "version": "1.0.0" }

@app.on_event("startup")
async def startup():
  await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
  await prisma.disconnect()