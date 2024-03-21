#!/usr/bin/python3
from models.user import User
from models.base_model import BaseModel

class FileStorage:
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        met = str(obj.__class__.__name__) + '.' + str(obj.id)
        self.__objects[met] = obj

    def save(self):
        from json import dump

        file_name = self.__file_path

        to_json = dict(self.__objects)
        for k, v in to_json.items():
            to_json[k] = v.to_dict()

        with open(file_name, "w", encoding="UTF-8") as f:
            dump(to_json, f)

    def reload(self):
        from json import load
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                from_json = load(file)
                self.__objects = dict(from_json)
        except FileNotFoundError:
            pass
