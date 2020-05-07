from django.db import models
from django.utils import timezone

from .model_Publication import Publication
from .model_Profile import Profile

class StateOfBook(models.Model):

    reading='10'
    future_reading='20'
    finished='30'
    AC_CHOICES= (
        (reading, 'reading'),
        (future_reading, 'future_reading'),
        (finished, 'finished')
    )

    date= models.DateField(default=timezone.now)
    state = models.CharField( max_length=2, choices=AC_CHOICES, default=finished)
    book = models.ForeignKey(Publication, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together= ('book', 'profile') 
         
    def publish(self):
        self.save()

    def __str__(self):
        return self.state