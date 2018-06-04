"""
This file contains tests for the app.py file that contains my api endpoints
"""
from flask_testing import TestCase
from run import app
import json

class TestRun(TestCase):

    def create_app(self):
        return app

    def test_create_request(self):
        with self.client:
            response = self.client.post("/1/users/requests", content_type='application/json',
                                        data=json.dumps(dict(
                                            request_title="Fix iphone", 
                                            request_description="iphone screen needs fixing",
                                            requester_name="Gideon B",
                                            req_id=1))
                                        )            
            reply = json.loads(response.data.decode())
            self.assertEquals(reply["message"], "sucessfully created request")
            self.assertEquals(response.status_code, 200)

    def test_fetch_requests(self):
        with self.client:
            response = self.client.get("/1/users/requests")
            reply = json.loads(response.data.decode())
            self.assertEquals(reply["message"], "Successfully fetched requests")
            self.assertEquals(response.status_code, 200)

    def test_fetch_a_request(self):
        with self.client:
            response = self.client.get("/1/users/requests/1")
            reply = json.loads(response.data.decode())
            self.assertEquals(reply["message"], "Successfully fetched the request")
            self.assertEquals(response.status_code, 200)
    
    def test_edit_request(self):
        with self.client:
            response = self.client.put(
                "/1/users/requests/1",
                content_type='application/json',
                data=json.dumps(dict(
                    request_title="Fix Car",
                    request_description="iphone screen needs fixing"))
                    )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Successfully edited the request")
        self.assertEquals(response.status_code, 200)

    def test_fetch_app_requests(self):
        """ Test for endpoint that fetches all requests on the application"""
        with self.client:
            response = self.client.get("api/v1/requests")
            reply = json.loads(response.data.decode())
            self.assertEquals(response.status_code, 200)
        pass
    
    def test_approve_request(self):
        pass
    
    def test_dispprove_request(self):
        pass
    
    def test_resolve_request(self):
        pass