#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """A class representing a user with basic attributes

    Attributes:
   (str) email : The email of the user
   (str) password : The password of the user
   (str) first_name : The first name of the user
   (str) last_name : The last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
