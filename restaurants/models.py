from django.db import models

class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	Opening_time = models.TimeField()
	Closing_time = models.TimeField()

	def __str__(self):
		return self.title




