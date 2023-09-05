#!/usr/bin/python3
"""Defines the Payment class."""
from models.base_model import BaseModel

class Payment(BaseModel):
    """Represents a payment.

    Attributes:
        user_id (str): The ID of the user making the payment.
        cart_id (str): The ID of the cart associated with the payment.
        payment_method (str): The type of payment method used.
        payment_date (str): The date and time the payment was made.
        payment_status (str): The status of the payment.
        transaction_id (str): The ID of the transaction associated with the payment.
    """

    user_id = ""
    cart_id = ""
    payment_method = ""
    payment_date = ""
    payment_status = ""
    transaction_id = ""

    def __init__(self, *args, **kwargs):
        """Initialize Payment instance."""
        super().__init__(*args, **kwargs)
        if 'user_id' in kwargs:
            self.user_id = kwargs['user_id']
        if 'cart_id' in kwargs:
            self.cart_id = kwargs['cart_id']
        if 'payment_method' in kwargs:
            self.payment_method = kwargs['payment_method']
        if 'payment_date' in kwargs:
            self.payment_date = kwargs['payment_date']
        if 'payment_status' in kwargs:
            self.payment_status = kwargs['payment_status']
        if 'transaction_id' in kwargs:
            self.transaction_id = kwargs['transaction_id']

    def __str__(self):
        """Return string representation of Payment instance."""
        return "[Payment] ({}) User: {} - Method: {} - Status: {}".format(
            self.id, self.user_id, self.payment_method, self.payment_status)

    def to_dict(self):
        """Return dictionary representation of Payment instance."""
        payment_dict = super().to_dict()
        payment_dict['user_id'] = self.user_id
        payment_dict['cart_id'] = self.cart_id
        payment_dict['payment_method'] = self.payment_method
        payment_dict['payment_date'] = self.payment_date
        payment_dict['payment_status'] = self.payment_status
        payment_dict['transaction_id'] = self.transaction_id
        return payment_dict

    def from_dict(self, data_dict):
        """Update Payment instance from dictionary."""
        super().from_dict(data_dict)
        if 'user_id' in data_dict:
            self.user_id = data_dict['user_id']
        if 'cart_id' in data_dict:
            self.cart_id = data_dict['cart_id']
        if 'payment_method' in data_dict:
            self.payment_method = data_dict['payment_method']
        if 'payment_date' in data_dict:
            self.payment_date = data_dict['payment_date']
        if 'payment_status' in data_dict:
            self.payment_status = data_dict['payment_status']
        if 'transaction_id' in data_dict:
            self.transaction_id = data_dict['transaction_id']
