from django.db import models
from django.utils import timezone

class CreditCards(models.Model):
    number = models.CharField(max_length=16, primary_key=True)
    cod = models.IntegerField()
    card_name = models.CharField(max_length=50)
    date_expiration = models.DateField(auto_now=False, auto_now_add=False)
    bank = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.card_name