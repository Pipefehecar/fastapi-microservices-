from typing import List, Optional
from pydantic import BaseModel

class CarIn(BaseModel):
    name: str
    description: str
    year: int
    manufacturer_id: int
    categories: List[str]
    features: List[str]

class CarOut(CarIn):
    id: int

class CarUpdate(CarIn):
    name: Optional[str] = None
    description: Optional[str] = None
    year: Optional[int] = None
    manufacturer_id: Optional[int] = None
    categories: Optional[List[str]] = None
    features: Optional[List[str]] = None