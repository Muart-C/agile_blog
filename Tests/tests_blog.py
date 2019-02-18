import unittest
from app.blog import Users, Comments

class UsersTestClass (unittest.TestCase):
    def setUp(self):
        self.myuser = User("Joe")

    def test_getname(self):
        self.assertEqual(self.myuser.get_name(), "Joe")
    
    def test_login(self):
        self.assertTrue(self.myuser.is_logged_in())
    


class CommentsTestClass(unittest.TestCase):

    def setUp(self):
        self.mycomment= Comment("Joe", "Home is here", None)
    
    def test_replied_to(self):
        self.assertisNone(self.mycomment.replied_to())
    
    def test_to_string(self):
        self.assertIsInstance(self.mycomment.to_string(), str)

