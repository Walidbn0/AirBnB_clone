#!/usr/bin/python3from models.base_models import BaseModel

class City(BaseModel):
    """A class that represents a city

    Attributes:
       (str) name : name of the city
       (str) state_id : the state id
    """
    state_id = ""
    name = ""
