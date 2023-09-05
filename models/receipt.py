#!/usr/bin/python3
"""Receipt module for the Dunta project."""
from models.base_model import BaseModel
from models.user import User

class Receipt(BaseModel):
    """Represent a Receipt.
    Attributes:
        product_ids (list): List of product IDs purchased.
        delivery_time (str): The estimated delivery time.
        payment_status (str): A note indicating payment status (e.g., "Payment successful").
        payment_date (str): The date of payment.
        company_name (str): The name of the company.
        user_name (str): The name of the user.
        user_address (str): The address of the user including city, state, and zip code.
    """

    product_ids = []
    delivery_time = ""
    payment_status = ""
    payment_date = ""
    company_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Receipt instance"""
        super().__init__(*args, **kwargs)
        user = User.get(self.user_id)
        user_address_parts = [user.address, user.city, user.state, user.zip_code]
        self.user_address = ", ".join(filter(None, user_address_parts))
        self.user_name = user.first_name + " " + user.last_name
