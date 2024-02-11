#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import models
from models.user import User
import unittest
from datetime import datetime
from time import sleep


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def setUp(self):
        self.user_model = User()

    def tearDown(self):
        del self.user_model
    
    def test_instance_creation(self):
        self.assertIsInstance(self.user_model, User)
        self.assertTrue(hasattr(self.user_model, 'id'))
        self.assertTrue(hasattr(self.user_model, 'created_at'))
        self.assertTrue(hasattr(self.user_model, 'updated_at'))
        self.assertTrue(hasattr(self.user_model, 'email'))
        self.assertTrue(hasattr(self.user_model, 'password'))
        self.assertTrue(hasattr(self.user_model, 'first_name'))
        self.assertTrue(hasattr(self.user_model, 'last_name'))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(self.user_model.updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(self.user_model.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(self.user_model.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(self.user_model.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(self.user_model.last_name))

    def test_two_users_unique_ids(self):
        us1 = self.user_model
        us2 = self.user_model
        self.assertNotEqual(us1.id, us2.id)

    def test_two_users_different_created_at(self):
        us1 = self.user_model
        sleep(0.05)
        us2 = self.user_model
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_different_updated_at(self):
        us1 = self.user_model
        sleep(0.05)
        us2 = self.user_model
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        us = self.user_model
        us.id = "123456"
        us.created_at = us.updated_at = dt
        usstr = us.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)



if __name__ == "__main__":
    unittest.main()