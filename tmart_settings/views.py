from django.shortcuts import render
from django.views.generic import ListView
from .models import OurInformation
# Create your views here.

class Contact(ListView):
	template_name = 'settings/contact.html'
	def get_queryset(self):
		return OurInformation.objects.filter(active = True).first()