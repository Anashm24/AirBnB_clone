#!/usr/bin/python3
"""A script that creates a User class."""

# Import necessary modules
from models.base_model import BaseModel


class Amenity(BaseModel):
    """represent the amenity

    Attributes:
        name (str): The name of the amenity.
    """

    name: str = ""
