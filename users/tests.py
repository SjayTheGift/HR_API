from django.test import TestCase
from django.contrib.auth import get_user_model
import json

User = get_user_model()

test_users = [
    {"email": "testuser1@me.com", "password": "testpassword1"},
    {"email": "testuser2@gmail.com", "password": "testpassword2"},
]

class LoginTest(TestCase):
    def setUp(self):
        for user in test_users:
            new_user = User.objects.create(email=user["email"])
            new_user.set_password(user["password"])
            new_user.save()

    def test_login(self):
        USER1 = test_users[0]
        res = self.client.post('/api/login/',
                               data=json.dumps({
                                   'email': USER1["email"],
                                   'password': USER1["password"],
                               }),
                               content_type='application/json',
                               )
        result = json.loads(res.content)
        self.assertTrue("access" in result)