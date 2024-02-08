#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
            String repr
        """
        return "[{}] ({}) {}]".format(self.__class__.__name__,self.id,self.__dict__)