#!/usr/bin/python3
"""Defines the Product class."""
from models.base_model import BaseModel

class Product(BaseModel):
    """Represents a Product.

    Attributes:
        name (str): The name of the product.
        description (str): The description of the product.
        price (float): The price of the product.
        category (str): The category of the product.
        image (str): The URL of the product image.
        tags (list): A list of tags for the product.
        rating (float): The average rating of the product.
        reviews (list): A list of reviews for the product.
        date_added (str): The date the product was added to the database.
        date_updated (str): The date the product was last updated.
    """

    name = ""
    description = ""
    price = 0.0
    category = ""
    image = ""
    tags = []
    rating = 0.0
    reviews = []
    date_added = ""
    date_updated = ""

    def __init__(self, *args, **kwargs):
        """Initialize Product instance."""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return string representation of Product instance."""
        return "[Product] ({}) {}".format(self.id, self.name)

    def to_dict(self):
        """Return dictionary representation of Product instance."""
        product_dict = super().to_dict()
        product_dict['category'] = self.category
        product_dict['image'] = self.image
        product_dict['tags'] = self.tags
        product_dict['rating'] = self.rating
        product_dict['reviews'] = self.reviews
        product_dict['date_added'] = self.date_added
        product_dict['date_updated'] = self.date_updated
        return product_dict

    def from_dict(self, data_dict):
        """Update Product instance from dictionary."""
        super().from_dict(data_dict)
        if 'category' in data_dict:
            self.category = data_dict['category']
        if 'image' in data_dict:
            self.image = data_dict['image']
        if 'tags' in data_dict:
            self.tags = data_dict['tags']
        if 'rating' in data_dict:
            self.rating = data_dict['rating']
        if 'reviews' in data_dict:
            self.reviews = data_dict['reviews']
        if 'date_added' in data_dict:
            self.date_added = data_dict['date_added']
        if 'date_updated' in data_dict:
            self.date_updated = data_dict['date_updated']
