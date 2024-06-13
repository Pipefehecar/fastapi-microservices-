from fastapi import FastAPI

from app.api.cars import cars

app = FastAPI()

app.include_router(cars)
