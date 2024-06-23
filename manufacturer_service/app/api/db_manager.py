from app.api.models import ManufacturerIn
from app.api.db import manufacturers, database


async def add_manufacturer(payload: ManufacturerIn):
    query = manufacturers.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_manufacturer(id):
    query = manufacturers.select(manufacturers.c.id==id)
    return await database.fetch_one(query=query)