from django.db import models
from django.urls import reverse
# Create your models here.
class Company(models.Model):
	company_name = models.CharField(max_length=40)
	company_logo = models.FileField(null='True',blank='True')
	company_city = models.CharField(max_length=40)
	
	def __str__(self):
		return self.company_name