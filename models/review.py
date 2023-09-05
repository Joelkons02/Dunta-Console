#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review.

    Attributes:
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.
        rating (float): The rating of the product given by the user.
        date_created (str): The date and time the review was created.
        date_updated (str): The date and time the review was last updated.
    """

    user_id = ""
    text = ""
    rating = 0.0
    date_created = ""
    date_updated = ""

    def __init__(self, *args, **kwargs):
        """Initialize Review instance."""
        super().__init__(*args, **kwargs)
        if 'user_id' in kwargs:
            self.user_id = kwargs['user_id']
        if 'text' in kwargs:
            self.text = kwargs['text']
        if 'rating' in kwargs:
            self.rating = kwargs['rating']
        if 'date_created' in kwargs:
            self.date_created = kwargs['date_created']
        if 'date_updated' in kwargs:
            self.date_updated = kwargs['date_updated']

    def __str__(self):
        """Return string representation of Review instance."""
        return "[Review] ({}) User: {} - Rating: {}".format(
            self.id, self.user_id, self.rating)

    def to_dict(self):
        """Return dictionary representation of Review instance."""
        review_dict = super().to_dict()
        review_dict['user_id'] = self.user_id
        review_dict['text'] = self.text
        review_dict['rating'] = self.rating
        review_dict['date_created'] = self.date_created
        review_dict['date_updated'] = self.date_updated
        return review_dict

    def from_dict(self, data_dict):
        """Update Review instance from dictionary."""
        super().from_dict(data_dict)
        if 'user_id' in data_dict:
            self.user_id = data_dict['user_id']
        if 'text' in data_dict:
            self.text = data_dict['text']
        if 'rating' in data_dict:
            self.rating = data_dict['rating']
        if 'date_created' in data_dict:
            self.date_created = data_dict['date_created']
        if 'date_updated' in data_dict:
            self.date_updated = data_dict['date_updated']
