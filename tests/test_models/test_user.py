#!/usr/bin/python3
"""test module for class user"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User"""

    def setUp(self):
        self.user = User()

    def test_init(self):
        """Test User class initialization"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attr_types(self):
        """Test data types of User attributes"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_to_dict(self):
        """Test conversion of User instance to dictionary"""
        user_dict = self.user.to_dict()
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertEqual(user_dict["email"], "")
        self.assertEqual(user_dict["password"], "")
        self.assertEqual(user_dict["first_name"], "")
        self.assertEqual(user_dict["last_name"], "")

    def test_str_representation(self):
        """Test the __str__ representation of User"""
        expected_str = (
            "[User] ({}) {{'id': '{}', 'created_at': '{}', "
            "'updated_at': '{}', 'email': '{}', "
            "'password': '{}', 'first_name': '{}', 'last_name': '{}'}}"
        ).format(
            user.id, user.id, user.created_at, user.updated_at,
            user.email, user.password, user.first_name, user.last_name
        )
        self.assertEqual(str(self.user), expected_str)

    def test_update_attributes(self):
        """Test updating User attributes"""
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_update_attributes_to_dict(self):
        """Test updating attributes and conversion to dictionary"""
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "password123")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")


if __name__ == '__main__':
    unittest.main()
