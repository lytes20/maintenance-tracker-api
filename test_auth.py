from flask_testing import TestCase
from run import app
import json


class UserAuthTest(TestCase):

    def create_app(self):
        return app

    def test_register(self):
        """ Test for successful user login """
        with self.client:
            response = self.client.post(
                "/user/register",
                content_type='application/json',
                data=json.dumps(dict(username="Gideon B", email="email@email.com", password="secret"))
                )            
            reply = json.loads(response.data)
            self.assertEquals(reply["message"], "successfully registered")
            self.assertEquals(response.status_code, 201)