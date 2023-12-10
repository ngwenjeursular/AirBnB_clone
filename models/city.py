#!/usr/bin/python3
"""  this module defines the city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """This is the City class."""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize City instance."""
        super().__init__(*args, **kwargs)
