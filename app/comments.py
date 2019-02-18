from datetime import datetime
from collections import namedtuple


class Comment:

    chat_messages = []
    def __init__(self):
        # Comment Parameters
        self.messages = []
        self.replied_to =None


    def get_author(self):
        pass

    def set_message(self, message, author, replied_to =None):
        """Sets message"""
        message_received = namedtuple('message',['message','replied_to','author','create_at'])
        replied_to_value = ''
        if self.replied_to != None:
            replied_to_value = self.replied_to
        else: None
        if message != None and replied_to != None:
            message = message_received(message,replied_to_value,author,self.created_at)

        self.messages.append(message_received)
        self.chat_messages.append(message_received)

    def get_list(self):
        return self.messages

    def edit_message(self, id, newmessage):
        """Edits message"""
        for message in self.messages:
            if message["id"] == id:
                message["message"] = newmessage

    @property
    def replied_to(self):
        return self.replied_to 

    def created_at(self):
        return datetime.datetime.now()

    def to_string(self):
        pass

    def delete_comment(self, message_id):
        """Deletes comment from list"""
        # Check instance of message id is int and list is not empty
        if isinstance(message_id, int):
            for message in self.messages:
                # Check ids match
                if message['id'] == message_id:
                    self.messages.remove(message)
                    return 'Comment Deleted'
                return 'Comment Doesnt Exist'
        return 'Invalid Id'
