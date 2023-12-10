#!/usr/bin/python3
"""This module defines the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance."""
        super().__init__(*args, **kwargs)
