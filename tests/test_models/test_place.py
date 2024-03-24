import unittest
import os
import json
from datetime import datetime
from models.state import State

class TestStateInit(unittest.TestCase):

    def test_init_with_name(self):
        state = State(name="California")
        self.assertEqual(state.name, "California")
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertEqual(state.created_at, state.updated_at)

    def test_init_without_name(self):
        state = State()
        self.assertEqual(state.name, "")

class TestStateName(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_set_name(self):
        self.state.name = "New York"
        self.assertEqual(self.state.name, "New York")

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            self.state.name = 10

class TestStatePersistence(unittest.TestCase):

    def setUp(self):
        self.state = State(name="Texas")
        self.filename = f"{self.state.id}.json"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_and_to_dict(self):
        
        self.state.save()

        self.assertTrue(os.path.exists(self.filename))

        with open(self.filename, 'r') as f:
            data = json.load(f)

        self.assertEqual(data["name"], "Texas")
        self.assertIsInstance(data["created_at"], str)
        self.assertIsInstance(data["updated_at"], str)

        try:
            datetime.fromisoformat(data["created_at"])
            datetime.fromisoformat(data["updated_at"])
        except ValueError:
            self.fail("Saved timestamps are not in right format")

