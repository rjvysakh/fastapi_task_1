from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from fastapi_task_2.db.base import Base


class User(Base):
    """
    User class represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The unique username of the user.
        hashed_password (str): The hashed password of the user.
        created_at (DateTime): The timestamp indicating when the user was created.
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
