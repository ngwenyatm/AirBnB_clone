#!/usr/bin/python3
from datetime import datetime
import uuid

"""method is called when an instance is created"""

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
