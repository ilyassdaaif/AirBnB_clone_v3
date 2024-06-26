#!/usr/bin/python3
"""
City Module for AirBnB clone
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """ City class """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
