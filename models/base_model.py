#!/usr/bin/python3
from datetime import datetime
import uuid
import json

"""defines all common attributes/methods for other classes"""

class BaseModel:
    """
    if kwargs is not empty:
        each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute).
        each value of this dictionary is the value of this attribute name
        created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT:%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
    else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    """returns object as a str"""
    def __str__(self):
        return f"[{' '.join(self.__class__.__name__.split('_'))}] ({self.id}) {self.__dict__}"

    """serializes the object into a JSON string and saves it to a file"""
    def save(self):
        self.updated_at = datetime.utcnow()
        with open("{}.json".format(self.id), 'w') as f:
            json.dump(self.to_dict(), f)

    """returns a dictionary"""
    def to_dict(self):
        _dict = self.__dict__.copy()
        _dict['__class__'] = self.__class__.__name__
        _dict['created_at'] = self.created_at.isoformat()
        _dict['updated_at'] = self.updated_at.isoformat()
        return _dict

    """reads a JSON string from a file and reconstructs the 'BaseModel' object"""
    @staticmethod
    def load_from_file(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return BaseModel(**data)
