#!/usr/bin/python3
"""Defines STATE class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Representation of State

    Attributes:
              name(str): The state name
    """

    name = ""
