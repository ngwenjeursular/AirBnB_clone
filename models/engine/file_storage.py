#!/usr/bin/python3

"""This is the module for file storage
defining class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances:"""

import json
import os
import models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
# from models.user import User


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON file to instances:"""

    CLASSES = {
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    __file_path = "file.json"
    __objects = {}
    classes = {}

    def __init__(self):
        from models.base_model import BaseModel

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w') as file:
            obj_dict = {k: obj.to_dict() for k, obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised"""

        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)

                for value in obj_dict.values():
                    class_name = value.get("__class__")
                    if class_name:
                        self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
