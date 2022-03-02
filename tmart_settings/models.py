import email
from django.db import models
# Create your models here.

class IPs(models.Model):
	ip_address = models.GenericIPAddressField(blank = True , null = True)

class OurInformation(models.Model):
	address = models.TextField(verbose_name='آدرس')
	tel		= models.CharField(max_length=36)
	email	= models.EmailField(null=True , blank=True)
	copyright = models.CharField(max_length=150 , default='متن کپی رایت')
	active  = models.BooleanField()

	def __str__(self):
		return self.address