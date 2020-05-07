from django.db import models
from django.utils import timezone
from .model_KindOfDescription import *
from .model_Account import Account

class Profile(models.Model):
    account= models.ForeignKey(Account, on_delete=models.CASCADE)
    name= models.CharField( max_length=50)
    pleasures_gender = models.ManyToManyField(Gender, blank=True, null=True)
    pleasures_author = models.ManyToManyField(Author, blank=True, null=True)
    pleasures_editorial = models.ManyToManyField(Editorial,blank=True, null=True)
    
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name  

      