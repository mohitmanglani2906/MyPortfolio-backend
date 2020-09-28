from django.db import models
from django_mysql.models import ListCharField
from django.db.models import CharField


# Create your models here.

class Skills(models.Model):

    id = models.CharField(max_length=250, primary_key=True)
    skills_set = ListCharField(
        base_field=CharField(max_length=10),
        size=6,
        max_length=(6 * 11))
