from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	image = models.ImageField(null=True)
	opening_time = models.TimeField(auto_now_add=True)
	closing_time = models.TimeField(auto_now_add=True)
	img_url = models.URLField()
	publish_date = models.DateField(null=True)
	author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return self.name




class Item(models.Model):
	name = models.CharField(max_length=225)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=3)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

