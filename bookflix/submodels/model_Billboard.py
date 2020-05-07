from django.db import models
from django.utils import timezone
from .model_Account import Account

class Billboard(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    on_normal = models.BooleanField(default=False)
    on_premium = models.BooleanField(default=False)
    video=  models.URLField(   max_length=255, blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title