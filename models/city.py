#!/usr/bin/python3
"""Defines the City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Representation of the class of 'CITY'

    Attributes:
             state_id (str): state id
             name (str): Name of the city
    """

    state_id = ""
    name = ""
