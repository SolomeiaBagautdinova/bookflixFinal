from django.db import models
from django.utils import timezone

from .model_KindOfDescription import *

class Book(models.Model):
    isbn = models.IntegerField(primary_key=True)
    title = models.CharField( max_length=50)
    author= models.ForeignKey(Author, on_delete=models.CASCADE)
    genders = models.ManyToManyField(Gender)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    on_normal = models.BooleanField(default=False)
    on_premium = models.BooleanField(default=False)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title



