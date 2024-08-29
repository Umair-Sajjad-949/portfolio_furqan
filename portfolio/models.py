from django.db import models

# Create your models here.
class settings(models.Model):
    site_title= models.CharField(max_length=255)
    site_logo= models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    cover_title=models.CharField(max_length=255)
    cover_desc=models.TextField()
    about_title = models.TextField(max_length=255)
    about_desc=models.TextField()
    facebook=models.TextField(max_length=255) 
    linkdeIn=models.TextField(max_length=255)
    Instagram = models.TextField(max_length=255)
    email = models.EmailField(max_length=255)
    github = models.TextField(max_length=255) 
    