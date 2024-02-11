#!/usr/bin/python3
"""A script that creates a User class."""

# Import necessary modules
from models.base_model import BaseModel


class City(BaseModel):
    """Respresent a city

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id: str = ""
    name: str = ""
