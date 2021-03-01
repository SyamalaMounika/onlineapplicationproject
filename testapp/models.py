from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=40)
    original_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    category=models.CharField(max_length=30)
    image=models.CharField(max_length=200)