#!/usr/bin/python3
"""This module contains a class named State and City that inherit from
    the Base class.
    """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base
#Base = declarative_base()


class City(Base):
    """A class which is assign a table in MYSQL database

    It's has three class attributes(id, name and state_id)

    Note: state_id is a foreign key referencing states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
