from enum import Enum

class Faculty(Enum):
  SCIENCE = 1
  ENGINEERING = 2
  ARTS = 3
  AHS = 4
  MATHEMATICS = 5
  ENVIRONMENT = 6

class Expertise(Enum):
  CHEMISTRY = 1
  BIOLOY = 2
  PHYSICS = 3
  ENGLISH = 4
  MECHANICAL_ENGINEERING = 5
  ELECTRICAL_ENGINEERING = 6
  COMPUTER_ENGINEERING = 7
  ENVIRONMENT = 8
  

class Member:
  def __init__(self, first_name, last_name, faculty, wat_id, expertise, id):
    self.first_name = first_name
    self.last_name = last_name
    self.faculty = faculty
    self.watid = wat_id
    self.expertise = expertise
    self.id = id # student id
    
  def get_email(self):
    return "{}@uwaterloo.ca".format(self.wat_id)
    
class Post: 
  def __init__(self, author, date, post_message, expertise_required, id, replies):
    self.author = author
    self.date = date
    self.post_message = post_message
    self.expertise_required = expertise_required # list of enums
    self.id = id # match id in database
    self.replies = replies # list - default to empty list
    
  # send a private messag to the author
  def send_message_to_author(self, message):
    return 1
    
  # reply to post publicly
  def reply(self, replier, reply, date):
    reply = Reply(self, replier, reply, date)
    self.replies.append(reply)
  

class Reply:
  def __init__(self, post_replied_to, replier, reply, date)
    self.post_replied_to = post_replied_to # could be id of post in database
    self.replier = replier # Member
    self.reply = reply # a string -> the actual reply
    self.date = date
  
class Message:
  def __init__(self, sender, recepient, date, content, is_read):
    self.sender = sender # Member
    self.recipient = recipient # Member
    self.date = date # default to now if date is not provided
    self.content = content # the actual message 
    self.is_read = is_read # a bool indicating whether message is read
  
