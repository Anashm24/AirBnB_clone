#!/usr/bin/python3
"""defines a file storage class"""
import json
import os


class FileStorage():
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects[self.__class__.__name__.id] = obj
    
    def save(self):
        with open(self.__file_path, "w") as json_file:
            json.dump(self.__objects, json_file)
    
    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as json_file:
                self.__objects = json.load(json_file)
    
