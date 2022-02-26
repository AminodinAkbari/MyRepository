from urllib import response
from django.test import TestCase
from django.urls import reverse , resolve
from .views import *
from .models import *
# Create your tests here.

# class TestViews(TestCase):
#     def add_to_order_detail(self):
#         qs = Order.objects.create(is_paid=False)
#         response = self.client.get(reverse('add_to_order_detail' , args=['slug']))
#         self.assertEquals(response.status_code , 200)