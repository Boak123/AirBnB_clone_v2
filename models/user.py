#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")

class User(BaseModel, Base):
    """ user for the class """
    if (storage_engine == 'db'):
        __tablename__ = 'users'
        email = column(string(128), nullable=False)
        password = column(string(128), nullable=False)
        first_name = column(string(128), nullable=True)
        last_name = column(string(128), nullable=True)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

