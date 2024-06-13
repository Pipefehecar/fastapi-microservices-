from typing import List, Optional
from pydantic import BaseModel

class CarIn(BaseModel):
    name: str
    description: str
    year: int
    manufacturer: str
    categories: List[str]
    features: List[str]

class CarOut(CarIn):
    id: int

class CarUpdate(CarIn):
    name: Optional[str] = None
    description: Optional[str] = None
    year: Optional[int] = None
    manufacturer: Optional[str] = None
    categories: Optional[List[str]] = None
    features: Optional[List[str]] = None