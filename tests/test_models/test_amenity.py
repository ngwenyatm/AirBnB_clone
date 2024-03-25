import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity

class TestAmenityInit(unittest.TestCase):

    def test_init_no_args(self):
        """Tests initialization with no arguments."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertEqual(amenity.name, "")

    def test_init_with_args(self):
        """Tests initialization with arguments."""
        test_name = "Swimming Pool"
        amenity = Amenity(name=test_name)
        self.assertEqual(amenity.name, test_name)


class TestAmenityToDict(unittest.TestCase):

    def test_to_dict(self):
        """Tests if to_dict method returns a correct dictionary."""
        test_name = "Gym"
        amenity = Amenity(name=test_name)
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["name"], test_name)
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)
