from typing import List

from app.api.service import is_manufacturer_present
from app.api import db_manager
from app.api.models import CarIn, CarOut
from fastapi import APIRouter, HTTPException

cars = APIRouter()


@cars.get("/", response_model=List[CarOut])
async def index():
    return await db_manager.get_all_cars()


@cars.post("/", status_code=201)
async def add_car(payload: CarIn):
    if not is_manufacturer_present(payload.manufacturer_id):
        raise HTTPException(
            status_code=404, detail="Manufacturer with given id not found"
        )
    added_car = await db_manager.add_car(payload)
    return {"id": added_car, **payload.dict()}


@cars.put("/{id}")
async def update_car(id: int, payload: CarIn):
    car = await db_manager.get_car(id)
    if not car:
        raise HTTPException(status_code=404, detail="Car with given id not found")

    updated_data = payload.dict(exclude_unset=True)
    car_in_db = CarIn(**car)
    updated_car = car_in_db.copy(update=updated_data)
    return await db_manager.update_car(id, updated_car)


@cars.delete("/{id}")
async def delete_car(id: int):
    car = await db_manager.get_car(id)
    if not car:
        raise HTTPException(status_code=404, detail="Car with given id not found")
    return await db_manager.delete_car(id)
