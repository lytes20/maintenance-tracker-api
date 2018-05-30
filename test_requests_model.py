from flask_testing import TestCase
from run import app
import json
from models import MaintenanceRequest

class RequestModelTest(TestCase):

    def create_app(self):
        return app

    def test_create_request(self):
        req = MaintenanceRequest("Fix iPhone", "My iPhone's screen is broken, i might need a new one", "Gideon B", 124)
        self.assertEqual(req.title, "Fix iPhone")
        self.assertEqual(req.description, "My iPhone's screen is broken, i might need a new one")
        self.assertEqual(req.requester_name, "Gideon B")
        self.assertEqual(req.request_id, 124)

    def test_can_convert_to_json(self):
        req = MaintenanceRequest("Fix iPhone", "My iPhone's screen is broken, i might need a new one", "Gideon B", 124)
        resp = {
            "request_title": "Fix iPhone",
            "request_description":"My iPhone's screen is broken, i might need a new one",
            "requester_name": "Gideon B",
            "request_id":124
          }
        self.assertEqual(req.toJson(), resp)