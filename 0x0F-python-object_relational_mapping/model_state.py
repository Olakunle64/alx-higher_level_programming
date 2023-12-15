#!/usr/bin/python3
"""This module contains a class named State that inherit from
    the Base class.
    """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """A class which is assign a table in MYSQL database

    It's has two class attributes(id and name)
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
