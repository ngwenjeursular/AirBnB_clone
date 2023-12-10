#!/usr/bin/python3
"""Module for the base class of this project"""

import models
import uuid
from datetime import datetime
#from models import storage


class BaseModel:
    """This is the base model class for all other classes
    it defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the base model instances

        params:
            *args: positional arguments
            **kwargs(dictionary): allows a function
                        to accept any number of keyword args
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the class"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """For updating the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        if hasattr(self, 'updated_at'):
            obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__

        return obj_dict
