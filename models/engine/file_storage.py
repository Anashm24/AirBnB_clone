#!/usr/bin/python3
"""Defines a FileStorage class"""

# Import necessary modules
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    # Define the path to the JSON file
    __file_path = "file.json"
    # Initialize an empty dictionary to store objects
    __objects = {}

    def all(self):
        """Return all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Create a new object and add it to the dictionary"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Convert objects to dict format and save them to the JSON file"""
        json_objs = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(json_objs, json_file)

    def reload(self):
        """Load objects from the JSON file and add them to the dictionary"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                dict_objects = json.load(json_file)
                for obj in dict_objects.values():
                    cls = obj['__class__']
                    del obj['__class__']
                    key = f"{cls}.{obj['id']}"
                    FileStorage.__objects[key] = (eval(cls))(**obj)
