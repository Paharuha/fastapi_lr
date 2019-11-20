from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class WorkerBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    address: str
    password: str


class WorkerCreate(WorkerBase):
    pass


class Worker(WorkerBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    address: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class CallBase(BaseModel):
    call_date: datetime = None
    duration: int
    status: str
    worker_id: int
    user_id: int


class CallCreate(CallBase):
    pass


class Call(CallBase):
    id: int
    worker: Optional[Worker]
    user: Optional[User]

    class Config:
        orm_mode = True
