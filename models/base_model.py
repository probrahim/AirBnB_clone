#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):

        if kwargs:
            dt = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'update_at':
                    value = datetime.strptime(kwargs[key], dt)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat("T")
        obj_dict['updated_at'] = self.updated_at.isoformat("T")
        return obj_dict

    # Define first_name attribute
    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name
