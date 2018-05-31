"""
This file contains tests for the app.py file that contains my api endpoints
"""
from flask_testing import TestCase
from run import app
import json

class TestRun(TestCase):

    def create_app(self):
        return app

    def test_create_request(self): #req_title, req_desc, requester_name, req_id
        with self.client:
            response = self.client.post("1/users/requests", content_type='application/json',
                                        data=json.dumps(dict(
                                            request_title="Fix iphone", 
                                            request_description="iphone screen needs fixing",
                                            requester_name="Gideon B",
                                            req_id=1))
                                        )            
            reply = json.loads(response.data.decode())
            self.assertEquals(reply["message"], "sucessfully created request")

    def test_fetch_requests(self):
        with self.client:
            response = self.client.get("/users/requests")
            reply = json.loads(response.data.decode())
            self.assertEquals(reply["message"], "success")

    # def test_fetch_a_request(self):
    #     with self.client:
    #         response = self.client.get("/users/requests<requestid>")
    #         reply = json.loads(response.data.decode())
    #         self.assertEquals(reply["message"], "success")
    
    # def test_edit_request(self):
    #     with self.client.put("/users/requests/10", content_type='application/json', headers=headers, data=json.dumps(dict(title="something", desc="hasaja")))
    #     reply = json.loads(response.data)
    #     self.assertEquals(reply["message"], "Request Edited")