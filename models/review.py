#!/usr/bin/python3
"""A script that creates a User class."""

# Import necessary modules
from models.base_model import BaseModel


class Review(BaseModel):
    """represent the user review

    Attributes:
        place_id (str): The Place id
        user_id (str): The User id
        text (str): The text of the review
    """

    place_id: str = ""
    user_id: str = ""
    text: str = ""
