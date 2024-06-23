
from fastapi import FastAPI
from app.api.manufacturer import manufacturers
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(manufacturers, prefix='/api/v1/manufacturers', tags=['Manufacturer'])