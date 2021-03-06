from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email"""

        email = "test@test2.pl"
        password = "test123123"
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""

        email = "test@TEST2.pl"
        password = "test123123"
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with invalid email"""

        password = "test123123"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, password)

    def test_create_superuser(self):
        """Test creating superuser"""

        email = "test@test2.pl"
        password = "test123123"
        user = get_user_model().objects.create_superuser(email, password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
