from sqlalchemy import delete, select
from app.api.models import CarIn
from app.api.db import cars, database


async def add_car(payload: CarIn):
    query = cars.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_all_cars():
    query = cars.select()
    return await database.fetch_all(query=query)

async def get_car(id):
    query = select(cars).where(cars.c.id==id)
    return await database.fetch_one(query=query)

async def delete_car(id: int):
    query = delete(cars).where(cars.c.id==id)
    return await database.execute(query=query)

async def update_car(id: int, payload: CarIn):
    query = (
        cars
        .update()
        .where(cars.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)