""" Models script"""
class User:
    def __init__(self, name, email, password):
        self.username = name
        self.email= email
        self.password = password

class MaintenanceRequest:
    def __init__(self, title, desc, requester_name, request_id):
        """Initialise the MaintenanceRequest"""
        self.title = title
        self.description = desc
        self.requester_name = requester_name
        self.request_id = request_id
    
    def toJson(self):
        """Function to give the MaintenanceRequest model ability to be jsonified """
        res = dict(
            request_title=self.title,
            request_description = self.description,
            requester_name = self.requester_name,
            request_id = self.request_id
            )
        return res