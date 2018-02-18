from django.db import models

class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	opening_time = models.TimeField(auto_now_add=True)
	closing_time = models.TimeField(auto_now_add=True)
	img_url = models.URLField()

	def __str__(self):
		return self.name




