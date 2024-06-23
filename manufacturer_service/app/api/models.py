from pydantic import BaseModel
from typing import Optional

class ManufacturerIn(BaseModel):
    name: str
    nationality: Optional[str] = None


class ManufacturerOut(ManufacturerIn):
    id: int


class ManufacturerUpdate(ManufacturerIn):
    name: Optional[str] = None