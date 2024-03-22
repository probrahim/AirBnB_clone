#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.user import User

class Review(BaseModel):
    place_id = Place.id
    user_id = User.id
    text = ""
    