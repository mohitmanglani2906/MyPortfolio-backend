from django.db import models

# Create your models here.

class Intro(models.Model):

    profilePic = models.TextField(max_length=250)
    introduction = models.TextField(max_length=1000)


