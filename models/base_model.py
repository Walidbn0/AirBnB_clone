#!/usr/bin/python3
import uuid
from datetime import datetime

<<<<<<< HEAD
from base_model import models
=======
import models
>>>>>>> 42dca6ea594996f904d5c8bb69ac389a247468f5

class BaseModel:
    """BaseModels Class"""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """Update 'updated_at' with the current datetime to mark changes"""
        self.updated_at = datetime.now()
        models.storage.save(self)


    def to_dict(self):
        """Returns a dictionary of all instance attributes.
        """
        base_dict = {
            key: (value.isoformat() if isinstance(value, datetime) else value)
            for key, value in self.__dict__.items()
        }
        base_dict["__class__"] = self.__class__.__name__
        return base_dict
    def __str__(self) -> str:
        """should print/str representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

