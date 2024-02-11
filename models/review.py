#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
     """A class that represents a review

    Attributes:
       (str) place_id : The Place id.
       (str) user_id : The User id.
       (str) text : The text of the review.
    """
     place_id = ""
     user_id = ""
     text = ""
