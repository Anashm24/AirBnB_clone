#!/usr/bin/python3
"""defines a file storage class"""
import json
import os
from models.base_model import BaseModel


class FileStorage():
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        json_objects = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w+") as json_file:
            json.dump(json_objects, json_file)
    
    # def reload(self):
    #     try:
    #         with open(self.__file_path, "r") as json_file:
    #             FileStoragels.__objects = json.load(json_file)
    #     except FileNotFoundError as e:
    #         print(e)