"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import mock

from django.core.urlresolvers import resolve
from .views import index
from payments.views import sign_in
from django.shortcuts import render_to_response
from django.test import TestCase
from payments.models import User
from django.test import RequestFactory
from contact.views import contact

class MainPageTests(TestCase):

	@classmethod
	def setUpClass(cls):
		request_factory = RequestFactory()
		cls.request = request_factory.get('/')
		cls.request.session = {}

	def test_root_resolves_to_main_view(self):
		main_page = resolve('/')
		self.assertEqual(main_page.func, index)

	def test_contact_resolves_to_contact(self):
		contact_page = resolve('/contact/')
		self.assertEqual(contact_page.func, contact)

	def test_sign_in_resolves_to_views(self):
		sign_in_page = resolve('/sign_in')
		self.assertEqual(sign_in_page.func, sign_in)
	
	


	def test_index_returns_html_response_code_200(self):
		resp= index(self.request)
		self.assertEqual(resp.status_code, 200)

	def test_contact_returns_response_code_200(self):
		resp= contact(self.request)
		self.assertEqual(resp.status_code, 200)

	def test_returns_exact_html(self):
		resp= index(self.request)
		self.assertEquals(
			resp.content,
			render_to_response('index.html').content
		)

	def test_index_handles_logged_in_user(self):
# Create the user needed for user lookup from index page
# Note that we are not saving to the database
		

# Create a session that appears to have a logged in user
		self.request.session = {"user": "1"}

		with mock.patch('main.views.User') as user_mock:

# Tell the mock what to do when called
			config = {'get_by_id.return_value': mock.Mock()}
			user_mock.configure_mock(**config)

# Run the test
			resp = index(self.request)

# Ensure that we return the state of the session back to normal
			self.request.session = {}

			expected_html = render_to_response(
				'user.html', {'user': user_mock.get_by_id(1)})

			self.assertEquals(resp.content, expected_html.content)


