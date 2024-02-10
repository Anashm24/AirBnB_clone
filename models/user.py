#!/usr/bin/python3
"""A script that creates a User class."""

# Import necessary modules
from uuid import uuid4
from datetime import datetime
from base_model import BaseModel


class User(BaseModel):
    """class that inherits from BaseModel"""
    
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

    def __init__(self):
        super().__init__()