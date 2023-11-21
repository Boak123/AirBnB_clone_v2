#!/usr/bin/python3
"""
    module containing user class
    module containing user class
"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String
from os import environ
from models.base_model import Base

storage_engine = environ.get("HBNB_TYPE_STORAGE")

class User(BaseModel, Base):
    """
        User class for the user
        User class for the user
    """
    if (storage_engine == 'db'):
        __tablename__ = 'users'
        email = column(string(128), nullable=False)
        password = column(string(128), nullable=False)
        first_name = column(string(128), nullable=True)
        last_name = column(string(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

