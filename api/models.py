from distutils.command.upload import upload
from pyexpat import model
from django.db import models


class About(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="portfolio")
    email = models.EmailField(null=True)
    phone = models.BigIntegerField(null=True)
    age = models.IntegerField(null=True)
    jobTitle = models.JSONField(null=True)
    
    def __str__(self):
        return self.name
    


class Project(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    
    def __str__(self):
        return self.name
    
    
    
class About(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)
    
    def __str__(self):
        return self.name