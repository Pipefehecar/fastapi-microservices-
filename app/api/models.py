from typing import List
from pydantic import BaseModel

class Car(BaseModel):
    name: str
    description: str
    year: int
    manufacturer: str
    categories: List[str]
    features: List[str]