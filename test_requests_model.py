from flask_testing import TestCase
from run import app
import json
from models import Request

class RequestModelTest(TestCase):

    def create_app(self):
        return app

    def test_create_request(self):
        req = Request("Fix", "Desc", "user")
        self.assertEqual(req.title, "Fix")
        self.assertEqual(req.description, "Desc")
        self.assertEqual(req.requester_name, "user")