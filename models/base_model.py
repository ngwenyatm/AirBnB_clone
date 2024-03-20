#!/usr/bin/python3
"""
defines all common attributes/methods for other classes:
    """
from datetime import datetime
import uuid

class BaseModel:
    """BaseModel"""

    """returns object as a str"""
    def __str__(self):
        return f"[{' '.join(self.__class__.__name__.split('_'))}] ({self.id}) {self.__dict__}"

    """updates the public instance attribute"""
    def save(self):
        self.updated_at = datetime.utcnow()

    """returns a dictionary"""
    def to_dict(self):
        _dict = self.__dict__.copy()
        _dict['__class__'] = self.__class__.__name__
        _dict['created_at'] = self.created_at.isoformat()
        _dict['updated_at'] = self.updated_at.isoformat()
        return _dict
