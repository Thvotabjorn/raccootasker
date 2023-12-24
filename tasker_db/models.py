from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)

    tasks = relationship("Task", back_populates="author")


class Task(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    private = Column(Boolean, default=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime)

    author = relationship("User", back_populates="tasks")
    tasks = relationship("Timer", back_populates="task")


class Timer(Base):
    __tablename__ = "timers"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey('task.id'))
    end_time = Column(DateTime)
    created_at = Column(DateTime)

    tasks = relationship("Task", back_populates="timers")
