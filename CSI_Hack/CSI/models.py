from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AUDIO(models.Model):
	name = models.CharField(max_length=100)
	#file = models.FileField(blank=True)
	file = models.FileField(blank=True,upload_to='samples')
	transcript = models.TextField(blank=True)
