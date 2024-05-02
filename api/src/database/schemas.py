from pydantic import BaseModel
from datetime import datetime
from typing import List

class ProductBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    created_at: datetime


class TaskBase(BaseModel):
    title: str
    category: str
    description: str
    severity: str
    status: str
    contributors: str
    owner_id: int
    product_id: int

    class Config:
        orm_mode = True

class TaskCreate(TaskBase):
    id: int
    updated_at: datetime
    created_at: datetime


class UserBase(BaseModel):
    name: str
    email: str
    role: str
    affiliation: str

    class Config:
        orm_mode = True

class User(UserBase):
    hashed_password: str

class UserCreate(UserBase):
    id: int
    created_at: datetime
    access_token: str

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str