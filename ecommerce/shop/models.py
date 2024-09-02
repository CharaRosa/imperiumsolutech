from pickle import TRUE
from django.db import models
from django.db.models.fields.related import ForeignKey


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added= models.DateTimeField(auto_now=TRUE)
    class Meta:
        ordering=[
            '-date_added'
        ] 
    def __str__(self):
        return self.name   


class Product(models.Model):
    title = models.CharField(max_length=200)
    price= models.FloatField()
    description =models.TextField()
    category= ForeignKey(Category, related_name='categore', on_delete =models.CASCADE )
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.title 