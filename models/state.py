#!/usr/bin/python3
"""A script that creates a User class."""

# Import necessary modules
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state

    attributes: name"""

    name: str = ""
