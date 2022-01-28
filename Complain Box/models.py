from django.db import models

# Create your models here.


class Complain(models.Model):
	complain_message = models.CharField(max_length=200)
	#last_name = models.CharField(max_length=200)
	def __str__(self):
		return self.complain_message
