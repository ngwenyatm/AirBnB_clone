import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City

class TestCityInit(unittest.TestCase):

    def test_init_no_args(self):
        """Tests initialization with no arguments."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_init_with_args(self):
        """Tests initialization with arguments."""
        test_state_id = "1234"
        test_name = "Testville"
        city = City(state_id=test_state_id, name=test_name)
        self.assertEqual(city.state_id, test_state_id)
        self.assertEqual(city.name, test_name)

class TestCityToDict(unittest.TestCase):

    def test_to_dict(self):
        """Tests if to_dict method returns a correct dictionary."""
        test_state_id = "abcd"
        test_name = "Anytown"
        city = City(state_id=test_state_id, name=test_name)
        city_dict = city.to_dict()
        self.assertEqual(city_dict["state_id"], test_state_id)
        self.assertEqual(city_dict["name"], test_name)
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)

class TestCityFunctionality(unittest.TestCase):

    def test_update(self):
        """Tests update functionality."""
        city = City()
        new_state_id = "5678"
        new_name = "New City"
        city.state_id = new_state_id
        city.name = new_name
        self.assertEqual(city.state_id, new_state_id)
        self.assertEqual(city.name, new_name)
