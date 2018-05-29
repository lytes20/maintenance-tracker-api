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
            response = self.client.post("/", content_type='application/json',
                                        data=json.dumps(dict(title="something", desc="hasaja")))            
            reply = json.loads(response.data.decode())
            self.assertEquals(reply["message"], "sucessfully created request")