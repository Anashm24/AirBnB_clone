#!/usr/bin/python3
"""a script that creates a base model class"""

from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel():

    """defines all comon attributes and models for other classes
    """
    
    def __init__(self, *args, **kwargs):#
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if (key == "created_at" or key == "updated_at"):
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:            
            self.id = str(uuid4())
            if not hasattr(self, "created_at"):
                self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new()
        
                    
    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.now().isoformat()
        storage.save()
    
    def to_dict(self):
        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat(sep='T', timespec='auto')
        dictionary["updated_at"] = self.updated_at.isoformat(sep='T', timespec='auto')
        
        return dictionary

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)