#!/usr/bin/python3
"""A script that creates a base model class."""

# Import necessary modules
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """Defines all common attributes and methods for other classes."""

    def __init__(self, *args, **kwargs):
        # If kwargs is not empty, set the attributes using the key-value pairs
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        # Convert string to datetime object
                        value = datetime.fromisoformat(value)
                    # Set the attributes
                    setattr(self, key, value)
        else:
            # set the id, created_at, and updated_at attributes
            self.id = str(uuid4())
            if not hasattr(self, "created_at"):
                self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Add the new object to storage
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute and save the object to storage"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert the object to a dictionary"""
        _d = self.__dict__.copy()
        _d["__class__"] = self.__class__.__name__
        _d["created_at"] = self.created_at.isoformat(sep='T', timespec='auto')
        _d["updated_at"] = self.updated_at.isoformat(sep='T', timespec='auto')

        return _d
