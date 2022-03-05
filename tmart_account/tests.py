from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse , resolve
# Create your tests here.

class TestViews(TestCase):

	def setUp(self):
		User = get_user_model()
		user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

	def test_login(self):
		User = get_user_model()
		self.client.login(username='temporary', password='temporary')
		response = self.client.get(reverse('tmart_account:login'))
		user = User.objects.get(username='temporary')
		self.assertEquals(response.status_code , 302)
