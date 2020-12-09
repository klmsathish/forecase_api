from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_successfull(self):
        """Test: Creating new User with email [Successfull] """
        email = "test@test.com"
        username = "karan"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            username=username,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized"""
        username = "self",
        email = "self@user.com"
        user = get_user_model().objects.create_user(
            username=username, password="Test123", email=email)
        self.assertEqual(user.username, username)

    # def test_new_user_invalid_email(self):
    #     """"""
