"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .models import ContactForm
from datetime import datetime, timedelta


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class UserModelTest(TestCase):

	@classmethod
	def setUpClass(cls):
		ContactForm(email="test@dummy.com", name="test").save()
		ContactForm(email="j@j.com", name="jj").save()
		cls.firstUser = ContactForm(
			email="first@first.com",
			name="first",
			timestamp=datetime.today() + timedelta(days=2)
		)
		cls.firstUser.save()

	def test_contactform_str_returns_email(self):
		self.assertEquals("first@first.com", str(self.firstUser))


	def test_ordering(self):
		contacts = ContactForm.objects.all()
		self.assertEquals(self.firstUser, contacts[0])
