from typing import List

from fastapi import APIRouter, HTTPException

from app.api.models import Car
from cars_db import fake_car_db

cars = APIRouter()


@cars.get("/", response_model=List[Car])
async def index():
    return fake_car_db


@cars.post("/", status_code=201)
async def add_car(payload: Car):
    car = payload.dict()
    fake_car_db.append(car)
    return {"id": len(fake_car_db) - 1}


@cars.put("/{id}")
async def update_car(id: int, payload: Car):
    car = payload.dict()
    cars_length = len(fake_car_db)
    if 0 <= id <= cars_length:
        fake_car_db[id] = car
        return None
    raise HTTPException(status_code=404, detail="Car with given id not found")


@cars.delete("/{id}")
async def delete_car(id: int):
    cars_length = len(fake_car_db)
    if 0 <= id <= cars_length:
        del fake_car_db[id]
        return None
    raise HTTPException(status_code=404, detail="Car with given id not found")
