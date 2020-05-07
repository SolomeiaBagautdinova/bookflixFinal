from django.db import models
from django.utils import timezone

from .model_Publication import Publication

class CounterStates(models.Model):

    publication = models.ForeignKey(Publication, on_delete=models.CASCADE) 
    date_start = models.DateField( )
    date_start = models.DateField( )
    cant_reading = models.IntegerField(default=0)
    cant_future_read = models.IntegerField(default=0)
    cant_finished = models.IntegerField(default=0)

    
    def publish(self):
        self.save()