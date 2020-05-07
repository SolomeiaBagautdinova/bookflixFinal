from django.db import models
from django.utils import timezone
from .model_Profile import Profile
from .model_Publication import Publication

class Comment(models.Model):

    is_a_spoiler = models.BooleanField(default=False)
    description = models.TextField()
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)    


    def publish(self):
        self.save()

  
