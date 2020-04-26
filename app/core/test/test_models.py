from django.test import TestCase
from django.contrib.auth import get_user_model


class Modeltest(TestCase):
    def test_create_user_with_email_succesful(self):
        """Test creatin a new user with an email is succeful"""
        email = "darojas@mail.com"
        password = "123456"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,
                         email)
        self.assertTrue(user.check_password(password))
