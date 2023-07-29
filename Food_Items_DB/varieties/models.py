from django.db import models
from datetime  import datetime


class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class food(models.Model):
    Item_Image=models.ImageField(null=False, blank=False)
    Item_Name=models.CharField(max_length=100, null=False, blank=False)
    Item_Quantity=models.CharField(max_length=100,null=False, blank=False)
    Item_Category=models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    Item_Cost=models.DecimalField(max_digits=6, decimal_places=2)
    Item_Published=models.BooleanField(default=True)
    Manufactured_Date=models.DateTimeField(default=datetime.now, blank=True)
    Item_Review=models.TextField()
    def __str__(self):  
        return self.Item_Name








# Create your models here.
