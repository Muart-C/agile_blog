from datetime import datetime
from collections import namedtuple
from comments import Comment

class User:
  def __init__(self, name):
    self.name = name
    self._lobby = Comment(self.name)
    self._online_status = False
    self._last_seen = None
    self._class_received = self.__class__.__name__
  
  @property
  def get_name(self):
    return self.name
  
  @get_name.setter
  def set_name(self, value):
    self.name = value
  
  def is_logged_in(self):
    value = ''
    if self._online_status:
      value = 'Online: {} '.format(self._online_status)
    else:
      value = 'User is logged out by default'
      print(value)
      return value
  
  @property
  def last_logged_in_at(self):
    self._last_seen = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
  @property
  def log_in(self):
    self._online_status = True
    self.last_logged_in_at
  
  @property
  def log_out(self):
    self._online_status = False
  
  def login_error(self):
    contain_last_seen = 'please Login \nOnline: {} last seen @ {}'.format(self._online_status,self._last_seen)
    contain_only_status = 'please Login \nOnlne: {}'.format(self._online_status)
    login_error = contain_only_status if(self._last_seen == None) else contain_last_seen
    
    print(login_error)
    return login_error
  
  def can_edit(self, index='', comment=''):
    ## check if user is online
    if(self._online_status):
      message_pool = ''
      ## authorization check
      if (self._class_received == 'Moderator' or self._class_received == 'User'):
        ##can only edit own comment
        message_pool = self._lobby.get_message
      elif (self._class_received == 'Admin'):
        message_pool = self._lobby.to_string
      
      compliant_format = []
      
      for messages in message_pool:
        
        if(index != '' and comment != ''):
          try:
            if (message_pool == self._lobby.to_string):
              self.can_edit_lobby_comments(index,comment)
            elif(message_pool == self._lobby.get_message):
              self.can_edit_own_comments(index,comment)
          except IndexError:
            error = 'cannot edit at index is out of range'
            print(error)
            return error
          except Exception as e:
            error = 'cannot edit due to error: %s'%e
            print(error)
            return error
          else:
            return self.can_edit()
      else:
        if (messages.replied_to == None):
          value = '{} by {}'.format(messages.message,messages.author)
          compliant_format.append(value)
        else:
          value = '{} by {} (replied to {})'.format(messages.message,messages.author,messages.replied_to)
      print(compliant_format)
      return compliant_format
          
    else:
      self.login_error()
  
  def can_edit_own_comments(self,index,comment):
    message_received = namedtuple('message',['message','replied_to','author','create_at'])
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    old_comment = self._lobby.messages.pop(index)
    edit_comment = message_received(comment,old_comment.replied_to,self.name,current_time)
    
    ###get index of old comment in lobby comments
    old_comment_index = self._lobby.chat_messages.index(old_comment)
    
    ##remove from chat_messages the old comment
    self._lobby.chat_messages.pop(old_comment_index)
    ##insert in to lobby editted comment
    self._lobby.chat_messages.insert(old_comment_index,edit_comment)
    ##insert in to user_message editted comment
    self._lobby.messages.insert(index,edit_comment)
  
  def can_edit_lobby_comments(self,index,comment):
    message_received = namedtuple('message',['message','replied_to','author','create_at'])
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    old_comment = self._lobby.chat_messages.pop(index)
    edit_comment = message_received(comment,old_comment.replied_to,self.name,current_time)
    ###get index of old comment in lobby comments
    old_comment_index = self._lobby.chat_messages.index(old_comment)
    
    ##remove from chat_messages the old comment
    self._lobby.chat_messages.pop(old_comment_index)
    ##insert in to lobby editted comment
    self._lobby.chat_messages.insert(old_comment_index,edit_comment)
  
  def can_delete(self, index):
    if(self._online_status):
      if(self._class_received == 'Admin' or self._class_received == 'Moderator'):
        try:    
          self._lobby.chat_messages.pop(index)
        except IndexError:
            value ='cannot delete as index is out of range'
            print(value)
            return value
        except Exception as e:
            value='cannot delete due to error: %s'%e
            print(value)
            return value
        else:
            return self.to_string()
      else:
          value = 'cannot delete'
          print(value)
          return value
    else:
      self.login_error()

  def to_string(self,value='',reply_to=None):
    if(self._online_status):
      if value != '':
        self._lobby.set_replied_to(reply_to)
        self._lobby.set_message(value,self._lobby.get_author)
      else:
        compliant_format = []
        for chat_messages in self._lobby.to_string():
            if(chat_messages.replied_to == None):
                value = "{} by {}".format(chat_messages.message,chat_messages.author)
                compliant_format.append(value)
            else:
                value = "{} by {} (replied to {})".format(chat_messages.message,chat_messages.author,chat_messages.replied_to)
                compliant_format.append(value)

        print(compliant_format)
        return compliant_format
           
    else:
        self.login_error()  

class Moderator(User):
  
  def __init__(self, name):
    super().__init__(name)

class Admin(User):
  def __init__(self, name):
    super().__init__(name)

user = User("sam")
user.to_string("same")
user.can_edit_own_comments(1,"sdd")

