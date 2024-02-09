#!/usr/bin/ python3
"""A script that creates a base model class."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """Defines all common attributes and methods for other classes."""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            if not hasattr(self, "created_at"):
                self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat(sep='T', timespec='auto')
        dictionary["updated_at"] = self.updated_at.isoformat(sep='T', timespec='auto')

        return dictionary
