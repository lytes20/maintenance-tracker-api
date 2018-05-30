from flask_testing import TestCase
from run import app
import json


class UserAuthTest(TestCase):

    def create_app(self):
        return app

    def test_register(self):
        """ Test for successful user register """
        with self.client:
            response = self.client.post(
                "1/user/register",
                content_type='application/json',
                data=json.dumps(dict(username="Gideon B", email="email@email.com", password="secret"))
                )            
            reply = json.loads(response.data)
            self.assertEquals(reply["message"], "successfully registered")
            self.assertEquals(response.status_code, 201)

    def test_register_with_empty_password(self):
        """ Test for empty password validation """
        with self.client:
            response = self.client.post(
                "1/user/register",
                content_type='application/json',
                data=json.dumps(dict(username="Gideon B", email="email@email.com", password=""))
                )            
            reply = json.loads(response.data)
            self.assertEquals(reply["message"], "Missing password parameter")
            self.assertEquals(response.status_code, 400)

    def test_register_with_empty_username(self):
        """ Test for empty username validation """
        with self.client:
            response = self.client.post(
                "1/user/register",
                content_type='application/json',
                data=json.dumps(dict(username="", email="email@email.com", password="secret"))
                )            
            reply = json.loads(response.data)
            self.assertEquals(reply["message"], "Missing username parameter")
            self.assertEquals(response.status_code, 400)

    def test_register_with_empty_email(self):
        """ Test for empty email validation """
        with self.client:
            response = self.client.post(
                "1/user/register",
                content_type='application/json',
                data=json.dumps(dict(username="Gideon B", email="", password="secret"))
                )            
            reply = json.loads(response.data)
            self.assertEquals(reply["message"], "Missing email parameter")
            self.assertEquals(response.status_code, 400)

    def test_user_login_successfully(self):
        """ Test for login end point """
        with self.client:
            res = self.client.post(
                "1/user/register",
                content_type='application/json',
                data=json.dumps(dict(username="Gideon B", email="email@email.com", password="secret"))
                )            
            # reply = json.loads(res.data)

            response = self.client.post(
                "1/user/login",
                content_type='application/json',
                data=json.dumps(dict(email="email@email.com", password="secret"))
                )            
            reply = json.loads(response.data)

            self.assertEquals(reply["message"], "sucessfully logged in")
            self.assertEquals(response.status_code, 200)