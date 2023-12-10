#!/usr/bin/python3
"""module for the state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
        super().__init__(*args, **kwargs)
