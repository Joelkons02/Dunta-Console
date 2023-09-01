#!/usr/bin/python3
"""User module for the Dunta project."""
from models.base_model import BaseModel

class User(BaseModel):
    """Represent a User.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        address (str): The user's address.
        city (str): The city where the user resides.
        state (str): The state where the user resides.
        zip_code (str): The ZIP code of the user's location.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    address = ""
    city = ""
    state = ""
    zip_code = ""

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)
