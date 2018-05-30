""" Models script"""
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email= email
        self.password = password

class Request:
    def __init__(self, title, desc, requester_name):
        self.title = title
        self.description = desc
        self.requester_name = requester_name