import unittest
from app.users import User

class UsersTestClass (unittest.TestCase):
    def setUp(self):
        self.myuser = User("Joe")

    def test_getname(self):
        self.assertEqual(self.myuser.get_name(), "Joe")
    
    def test_login(self):
        self.assertTrue(self.myuser.login(False))

    def test_logout(self):
        self.assertFalse(self.myuser.logout(True))