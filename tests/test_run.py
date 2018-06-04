"""
This file contains tests for the app.py file that contains my api endpoints
"""
import json
from flask_testing import TestCase
from app import app


class TestRun(TestCase):    
    """ Class that contains the tests for the endpoints in app.views """

    def create_app(self):
        return app

    def test_create_request(self):
        """ Test for endpoint that creates a new request """
        with self.client:
            response = self.client.post("/1/users/requests", content_type='application/json',
                                        data=json.dumps(dict(
                                            request_title="Fix iphone", 
                                            request_description="iphone screen needs fixing",
                                            requester_name="Gideon B",
                                            req_id=1)))            
            reply = json.loads(response.data.decode())
            self.assertEqual(reply["message"], "sucessfully created request")
            self.assertEqual(response.status_code, 200)

    def test_fetch_requests(self):
        """ Test for endpoint that feteches requests for a logged in user """
        with self.client:
            response = self.client.get("/1/users/requests")
            reply = json.loads(response.data.decode())
            self.assertEqual(reply["message"], "Successfully fetched requests")
            self.assertEqual(response.status_code, 200)

    def test_fetch_a_request(self):
        """ Test for endpoint that feteches a request for a logged in user"""
        with self.client:
            response = self.client.get("/1/users/requests/1")
            reply = json.loads(response.data.decode())
            self.assertEqual(reply["message"], "Successfully fetched the request")
            self.assertEqual(response.status_code, 200)
    
    def test_edit_request(self):
        """ Test for endpoint that edits a request """
        with self.client:
            response = self.client.put(
                "/1/users/requests/1",
                content_type='application/json',
                data=json.dumps(dict(
                    request_title="Fix Car",
                    request_description="iphone screen needs fixing")))
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Successfully edited the request")
        self.assertEqual(response.status_code, 200)

    def test_fetch_app_requests(self):
        """ Test for endpoint that fetches all requests on the application"""
        with self.client:
            response = self.client.get("api/v1/requests")
            self.assertEqual(response.status_code, 200)
    
    def test_approve_request(self):
        """ Test for endpoint that approves a request """
        pass
    
    def test_dispprove_request(self):
        """ Test for endpoint that disapproves a request """
        pass
    
    def test_resolve_request(self):
        """ Test for endpoint that resolves a request """
        pass