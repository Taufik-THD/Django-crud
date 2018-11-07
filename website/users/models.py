from django.db import models
import json
# Create your models here.

class users(models.Model):
    username=models.CharField(max_length=25)
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=250)
    
    def __unicode__(self):
        data = {
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password
        }

        return json.dumps(data)
