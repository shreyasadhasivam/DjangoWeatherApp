from django.db import models

# Create your models here.

class City(models.Model):
	name = models.CharField(max_length=100)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9,decimal_places=6)
	country = models.CharField(max_length=100)

	def __str__(self):
		return self.name
