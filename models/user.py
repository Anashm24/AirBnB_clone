#!/usr/bin/python3
"""A script that creates a User class."""

# Import necessary modules
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
=======
    """class that inherits from BaseModel"""
>>>>>>> 5ed7f9613e0312cf833b6d7b40560ad24ee54dd8

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
<<<<<<< HEAD
=======

    def __init__(self):
        super().__init__()
>>>>>>> 5ed7f9613e0312cf833b6d7b40560ad24ee54dd8
