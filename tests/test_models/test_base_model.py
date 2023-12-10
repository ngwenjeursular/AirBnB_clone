#!/usr/bin/python3
"""Test cases suits for the Base model class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import json
import uuid
import os

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up any necessary test fixtures."""
        self.base_model = BaseModel()

    def tearDown(self):
        """Tear down any resources used by the test."""
        pass

    def test_id_is_string(self):
        """Test if the 'id' attribute is a string."""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """Test if the 'created_at' attribute is a datetime object."""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test if the 'updated_at' attribute is a datetime object."""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test if calling 'save' updates the 'updated_at' attribute."""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dict(self):
        """Test if 'to_dict' returns a dictionary."""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_includes_class_name(self):
        """Test if 'to_dict' includes the '__class__' key with class name."""
        obj_dict = self.base_model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_to_dict(self):
        """Test to_dict method"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('name', my_model_dict)
        self.assertIn('my_number', my_model_dict)
        if hasattr(my_model, 'updated_at'):
            self.assertIn('updated_at', my_model_dict)
        else:
            self.assertNotIn('updated_at', my_model_dict)

    def test_from_dict(self):
        """Test creation of instance from dictionary"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_dict = my_model.to_dict()

        new_model = BaseModel(**my_model_dict)

        self.assertIsInstance(new_model, BaseModel)
        self.assertNotEqual(new_model.id, my_model.id)
        self.assertNotEqual(new_model.created_at, my_model.created_at)
        self.assertEqual(new_model.name, my_model.name)
        self.assertEqual(new_model.my_number, my_model.my_number)
        self.assertNotEqual(new_model.updated_at, my_model.updated_at)

if __name__ == '__main__':
    unittest.main()
