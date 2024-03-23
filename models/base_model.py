#!/usr/bin/python3
from datetime import datetime
from models.__init__ import storage
import uuid
import json


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT:%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    """returns object as a str"""
    def __str__(self):
        return f"[{' '.join(self.__class__.__name__.split('_'))}]
    ({self.id}) {self.__dict__}"

    """serializes the object into a JSON string and saves it to a file"""
    def save(self):
        self.updated_at = datetime.now()
        with open("{}.json".format(self.id), 'w') as f:
            json.dump(self.to_dict(), f)
        storage.new(self)

    """returns a dictionary"""
    def to_dict(self):
        _dict = self.__dict__.copy()
        _dict['__class__'] = self.__class__.__name__
        _dict['created_at'] = self.created_at.isoformat()
        _dict['updated_at'] = self.updated_at.isoformat()
        return _dict

    """reads a JSON string from a file and reconstructs
    the 'BaseModel' object"""
    @staticmethod
    def load_from_file(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return BaseModel(**data)
