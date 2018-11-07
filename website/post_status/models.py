from django.db import models
import json

# Create your models here.

class status(models.Model):
    message=models.CharField(max_length=250)
    user_id=models.IntegerField()

class comments(models.Model):
    comment=models.CharField(max_length=250)
    user_id=models.IntegerField()
    status_id=models.IntegerField()
