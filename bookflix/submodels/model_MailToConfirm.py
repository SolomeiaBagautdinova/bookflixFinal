from django.db import models
from django.utils import timezone
from .model_Account import Account

class  MailToConfirm(models.Model):

    is_for_register= models.BooleanField(default=False)
    is_for_change = models.BooleanField(default=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_of_creation = models.DateTimeField(default=timezone.now)
   

    def publish(self):
        self.save()