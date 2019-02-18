import unittest
from app.comments import Comment

import datetime

class CommentsTestClass(unittest.TestCase):

    def setUp(self):
        self.mycomment= Comment()
        
    
    def test_set_message(self):
        self.mycomment.set_message("Joe", "We Her")
        self.assertEqual(len(self.mycomment.get_list()), 1)
    
    def test_delete_message(self):
        self.mycomment.set_message("Joe", "We Her")
        self.assertEqual(self.mycomment.delete_comment(0), "Comment Deleted")
    
    def test_delete_message_invalid(self):
        self.mycomment.set_message("Joe", "We Her")
        self.assertEqual(self.mycomment.delete_comment("a"), "Invalid Id")

    def test_delete_message_missing(self):
        self.mycomment.set_message("Joe", "We Her")
        self.assertEqual(self.mycomment.delete_comment(25), "Comment Doesnt Exist")


