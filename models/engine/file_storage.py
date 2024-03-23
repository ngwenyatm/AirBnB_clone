#!/usr/bin/python3
"""FileStorage class"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                loaded_objects = json.laod(file)
                for key, value in loaded_objects.items():
                    class_name, obj.id = key.split('.')
                    obj = BaseModel(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
