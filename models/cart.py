#!/usr/bin/python3
"""Cart module for the Dunta project."""
from models.base_model import BaseModel

class Cart(BaseModel):
    """Represent a Cart.
    Attributes:
        user_id (str): The ID of the user who owns the cart.
    """

    user_id = ""
