from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True


class TaskBase(BaseModel):
    title: str
    description: str
    private: bool


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class TimerBase(BaseModel):
    task_id: int
    end_time: datetime


class TimerCreate(TimerBase):
    pass


class Timer(TimerBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
