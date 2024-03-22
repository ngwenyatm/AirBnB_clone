#!/usr/bin/python3
import unittest
from datetime imort datetime, timedelta
import uuid
from models.base_model import BaseModel

class BaseModelTest(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_assigned_uuid(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertEqual(len(self.base_model.id), len(str(uuid.uuid4())))

    def test_created_at_is_assigned_current_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertAlmostEqual(self.base_model.created_at, datetime.now(), delta=timedelta(seconds=1))

    def test_updated_at_is_assigned_current_datetime_on_creation(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertAlmostEqual(self.base_model.updated_at, dateime.now(), delta=timedelta(seconds=1))

    def test_updated_at_is_updated_on_save(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertGreater(self.base_model.updated_at, original_updated_at)

    def test_str_method(self):
        expected_string = f"[{self.base_model.__class__.__name__}] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_string)

    def test_to_dict_method(self):
        expected_dict = 
        {
                'id': self.basse_model.id,
                'created_at': self.base_model.created_at.isoformat(),
                'updated_at': self.base_model.updated_at.isoformat(),
                '__class__': self.base_model.__class__.__name__
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

if __name__ == '__main_-':
    unittest.main()
