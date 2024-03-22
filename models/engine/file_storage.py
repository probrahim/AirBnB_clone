#!/usr/bin/python3
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        met = str(obj.__class__.__name__) + '.' + str(obj.id)
        self.__objects[met] = obj

    def save(self):
        """
        Serializes the __objects dictionary into 
        JSON format and saves it to the file specified by __file_path.
        """
        all_objs = FileStorage.__objects

        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        from json import load
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                from_json = load(file)
                self.__objects = dict(from_json)
        except FileNotFoundError:
            pass
