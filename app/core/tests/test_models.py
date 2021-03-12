from django.contrib.auth import get_user_model
from django.test import TestCase

class ModelTestss(TestCase):

  def test_create_user_with_email_successful(self):
    """Test creating a user with email is successful"""

    email = 'ujahemmanuel72@gmail.com'
    password = 'password'
    user = get_user_model().objects.create_user(
      email=email, 
      password=password
      )
    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))
  

  def test_user_email_normalized(self):
    """Tests user email is normalized"""
    email = 'ujahemmanuel72@GMAIL.COM'
    user = get_user_model().objects.create_user(email, 'password')
    self.assertEqual(user.email, email.lower())

  
  def test_user_email_invalid(self):
    """Test creating user with no email raises error"""
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user(None, 'password')
  
  def test_create_new_super_user(self):
    """Test creating a new superuser"""
    user = get_user_model().objects.create_superuser('ujahemmanuel72@gmail', 'password')
    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)