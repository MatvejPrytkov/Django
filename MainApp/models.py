from django.db import models
class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField() 
   description = models.TextField(max_length=370, default="Базовое описание")

# Create your models here.
