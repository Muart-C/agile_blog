import unittest
from app.comments import Comment
from app.users import User, Admin, Moderator

class UsersTestClass (unittest.TestCase):
    def setUp(self):
        self.mycomment= Comment()
        self.myuser = User("Joe")
        self.myadmin= Admin("Tow")

    def test_getname(self):
        self.assertEqual(self.myuser.get_name(), "Joe")
    
    def test_login(self):
        self.assertTrue(self.myuser.login(False))

    def test_log_out(self):
        self.assertFalse(self.myuser.log_out())
    
    def test_delete_comment(self):
        self.mycomment.set_message("Tow", "We Her")
        self.assertEqual(self.myadmin.delete_comment(self.mycomment, 0), "Comment Deleted")
    
    def test_delete_comment_user(self):
        self.mycomment.set_message("Joe", "She Him")
        self.assertEqual(self.myuser.delete_comment(self.mycomment, 0), "User Cannot Delete Comment")