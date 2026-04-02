"""
Validates incoming data
Prevents bad inputs from frontend
"""
from pydantic import BaseModel
from datetime import date

class CategoryCreate(BaseModel):
    name: str
    type: str


class CategoryOut(CategoryCreate):
    id: int

    class Config:
        from_attributes = True


class TransactionCreate(BaseModel):
    category_id: int
    amount: float
    date: date


class TransactionOut(TransactionCreate):
    id: int

    class Config:
        from_attributes = True