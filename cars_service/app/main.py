from fastapi import FastAPI

from app.api.cars import cars
from app.api.db import database, engine, metadata

metadata.create_all(engine)
app = FastAPI(openapi_url="/api/v1/cars/openapi.json", docs_url="/api/v1/cars/docs")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(cars, prefix='/api/v1/cars', tags=['Cars'])
