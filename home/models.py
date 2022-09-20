from django.db import models

# Create your models here.

class Order1(models.Model):
     name=models.CharField(max_length=40)
     address=models.CharField(max_length=50)
     pincode=models.IntegerField()
     state=models.CharField(max_length=15)

