#!/usr/bin/python3
"""Defines the CartItem class."""
from models.base_model import BaseModel
from models.product import Product

class CartItem(BaseModel):
    """Represents an item in a shopping cart.

    Attributes:
        cart_id (str): The ID of the cart.
        product_id (str): The ID of the product.
        quantity (int): The quantity of the product in the cart.
    """

    cart_id = ""
    product_id = ""
    quantity = 0

    def __init__(self, *args, **kwargs):
        """Initialize CartItem instance."""
        super().__init__(*args, **kwargs)
        if 'product_id' in kwargs:
            self.product_id = kwargs['product_id']
        if 'cart_id' in kwargs:
            self.cart_id = kwargs['cart_id']
        if 'quantity' in kwargs:
            self.quantity = kwargs['quantity']

    def __str__(self):
        """Return string representation of CartItem instance."""
        return "[CartItem] ({}) {} - Quantity: {}".format(
            self.id, self.product_id, self.quantity)

    def to_dict(self):
        """Return dictionary representation of CartItem instance."""
        cart_item_dict = super().to_dict()
        cart_item_dict['cart_id'] = self.cart_id
        cart_item_dict['product_id'] = self.product_id
        cart_item_dict['quantity'] = self.quantity
        return cart_item_dict

    def from_dict(self, data_dict):
        """Update CartItem instance from dictionary."""
        super().from_dict(data_dict)
        if 'cart_id' in data_dict:
            self.cart_id = data_dict['cart_id']
        if 'product_id' in data_dict:
            self.product_id = data_dict['product_id']
        if 'quantity' in data_dict:
            self.quantity = data_dict['quantity']

    def calculate_total_price(self):
        """Calculate the total price of the item."""
        product = Product.get(self.product_id)
        if product is not None:
            return product.price * self.quantity
        return 0

    def is_in_stock(self):
        """Check if the item is in stock."""
        product = Product.get(self.product_id)
        if product is not None:
            return self.quantity <= product.stock
        return False
