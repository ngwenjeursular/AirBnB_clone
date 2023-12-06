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

if __name__ == '__main__':
    unittest.main()
