from django.db import models
from user.choices import gender_type


class User(models.Model):
    name = models.CharField(max_length=20,blank=False)
    email = models.EmailField(blank=False)
    number = models.CharField(max_length=10,blank=False)
    gender = models.CharField(choices=gender_type)