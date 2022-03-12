from urllib import response
from django.test import TestCase
from django.urls import reverse , resolve
from .views import *
from .models import *
from django.contrib.auth.models import User
# Create your tests here.

class TestViews(TestCase):

	def setUp(self):
		self.user = User.objects.create(username = 'Admin' , password = 'aminamin_2018' , email = 'test@test.com')

	def test_add_to_order_detail(self):
		qs = Order.objects.create(owner = self.user,is_paid=False)
		response = self.client.get(reverse('add_to_order_detail' , args=['slug']))
		self.assertEquals(response.status_code , 302)

	def test_cart_user(self):
		response = self.client.get(reverse('CartUser'))
		self.assertEquals(response.status_code , 302)

	def test_add_to_favorite(self):
		Order.objects.create(owner = self.user,is_paid=False)
		response = self.client.get(reverse('add_to_favorite' , args=['slug']))
		self.assertEquals(response.status_code , 302)

	def test_checkout(self):
		Order.objects.create(owner = self.user,is_paid=False)
		response = self.client.get(reverse('checkout'))
		self.assertEquals(response.status_code , 302)