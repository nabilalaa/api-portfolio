from distutils.command.upload import upload
from django.db import models


class About(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    email = models.EmailField(null=True)
    phone = models.BigIntegerField(null=True)
    age = models.IntegerField(null=True)
    jobTitle = models.JSONField(null=True)
    
    def __str__(self):
        return self.name
    
