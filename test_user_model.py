from flask_testing import TestCase
from run import app


class UserModelTest(TestCase):

    def create_app(self):
        return app

    def test_create_user(self):
        """ Function to test that a user is created from the user model"""
        user = User("Gideon Bamuleseyo", "gideon@mail.com", "secret")
        self.assertEqual(user.name, "Gideon Bamuleseyo")
        self.assertEqual(user.email, "123")
        self.assertEqual(user.password, "gideon@mail.com")