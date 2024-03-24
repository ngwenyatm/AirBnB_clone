#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.jso "
        self.storage = FileStorage()
        self.storage.__FileStorage__file_path = self.file_path
        self.user1 = User(email="test1@example.com", password="password1",
                          first_name="Mary", last_name="Poppins")
        self.user2 = User(email="test2@exemple.com", password="password2",
                          first_name="Seth", last_name="Lee")

    def tearDown(self):
    if os.path.exists(self.file_path):
        os.remove(self.file_path)

    def test_save_and_reload(self):
        self.storage.new(self.user1)
        self.storage.new(self.user2)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

         self.assertEqual(len(new_storage.all()), 2)
        self.assertIn("User." + self.user1.id, new_storage.all())
        self.assertIn("User." + self.user2.id, new_storage.all())

        reloaded_user1 = new_storage.all()["User." + self.user1.id]
        reloaded_user2 = new_storage.all()["User." + self.user2.id]

        self.assertIsInstance(reloaded_user1, User)
        self.assertIsInstance(reloaded_user2, User)
        self.assertEqual(reloaded_user1.email, "test1@example.com")
        self.assertEqual(reloaded_user2.email, "test2@example.com")

    if __name__ == '__main__':
        unittest.main()

