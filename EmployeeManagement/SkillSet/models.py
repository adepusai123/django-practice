from django.db import models

# Create your models here.
class Skills(models.Model):
    emailid = models.EmailField(max_length=100)
    skills = models.TextField()