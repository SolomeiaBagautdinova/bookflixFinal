from django.db import models
from django.utils import timezone
from .model_Publication import Publication

class ExpirationDates(models.Model):

    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    expiration_normal= models.DateField(blank=True, null=True)
    expiration_premium= models.DateField(blank=True, null=True)

    def publish(self):
        self.save()


class   UpDates(models.Model):
    
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    up_normal= models.DateField(blank=True, null=True)
    up_premium= models.DateField(blank=True, null=True)

    def publish(self):
        self.save()
