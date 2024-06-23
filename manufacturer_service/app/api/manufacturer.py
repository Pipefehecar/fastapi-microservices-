from app.api import db_manager
from app.api.models import ManufacturerIn, ManufacturerOut
from fastapi import APIRouter, HTTPException

manufacturers = APIRouter()


@manufacturers.post("/", response_model=ManufacturerOut, status_code=201)
async def create_manufacturer(payload: ManufacturerIn):
    manufacturer_id = await db_manager.add_manufacturer(payload)

    response = {"id": manufacturer_id, **payload.dict()}

    return response


@manufacturers.get("/{id}/", response_model=ManufacturerOut)
async def get_manufacturer(id: int):
    manufacturer = await db_manager.get_manufacturer(id)
    if not manufacturer:
        raise HTTPException(status_code=404, detail="Manufacturer not found")
    return manufacturer
