#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
    """BaseModels Class"""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def __str__(self):
        """String representation of the object. it returns a formatted string containing the class name, instance id, 
    and a dictionary representation of the object's attributes.
    """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update 'updated_at' with the current datetime to mark changes"""
        self.updated_at = datetime.now()
        models.storage.save(self)

    def to_dict(self):
        """Returns a dictionary of all instance attributes.
        """
        obj_dict = {key: value for key, value in self.__dict__.items() if not key.startswith('_')}
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

