from django.db import models
from django.utils import timezone
from .model_Profile import Profile
from .model_Publication import Publication
from .model_Comment import Comment


class Like(models.Model):
    
    is_like = models.BooleanField(default = False)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('author', 'publication')

    def publish(self):
        self.save()




class LikeComment(models.Model):
    
    is_like = models.BooleanField(default = False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('author', 'comment')

    def publish(self):
        self.save()


