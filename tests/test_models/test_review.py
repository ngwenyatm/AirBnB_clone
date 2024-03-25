import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review

class TestReviewInit(unittest.TestCase):

    def test_init_no_args(self):
        """Tests initialization with no arguments."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_init_with_args(self):
        """Tests initialization with arguments."""
        test_place_id = "123e45"
        test_user_id = "567f89"
        test_text = "This place is great!"
        review = Review(place_id=test_place_id, user_id=test_user_id, text=test_text)
        self.assertEqual(review.place_id, test_place_id)
        self.assertEqual(review.user_id, test_user_id)
        self.assertEqual(review.text, test_text)


class TestReviewToDict(unittest.TestCase):

    def test_to_dict(self):
        """Tests if to_dict method returns the correct dictionary."""
        test_place_id = "abcd"
        test_user_id = "efgh"
        test_text = "Lovely experience."
        review = Review(place_id=test_place_id, user_id=test_user_id, text=test_text)
        review_dict = review.to_dict()
        self.assertEqual(review_dict["place_id"], test_place_id)
        self.assertEqual(review_dict["user_id"], test_user_id)
        self.assertEqual(review_dict["text"], test_text)
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)
