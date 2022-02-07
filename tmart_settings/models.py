from django.db import models
# Create your models here.

class IPs(models.Model):
	ip_address = models.GenericIPAddressField(blank = True , null = True)