#!/usr/bin/python3
from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    state_id = State.id
    name=""
