from django.db import models
from django.utils import timezone

from .model_KindOfDescription import *
from .model_Account import Account


"""Se guardan la clase publicación y sus hijos, libro, libro por capítulo, billboard, chapter """

"-------Publication-------"
class Publication(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField()
    on_normal = models.BooleanField(default=False)
    on_premium = models.BooleanField(default=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

"-------Book-------"
class Book(models.Model):
    isbn = models.IntegerField(primary_key=True)
    author= models.ForeignKey(Author, on_delete=models.CASCADE)
    genders = models.ManyToManyField(Gender)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    url = models.URLField( max_length=200, blank=True, null=True)
    publication= models.OneToOneField(Publication, on_delete=models.CASCADE)

    def publish(self):
        self.save()

 
"-------BookByChapter-------"
class BookByChapter(models.Model):
    book= models.OneToOneField(Book, on_delete=models.CASCADE)
    cant_chapter = models.IntegerField(default = 1)
    
    def publish(self):
        self.save()


"-------Billboard-------"
class Billboard(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    video=  models.URLField(   max_length=255, blank=True, null=True)

    def publish(self):
        self.save()

"-------Chapter-------"
class Chapter(models.Model):
    number = models.IntegerField(default=0)
    book= models.ForeignKey(BookByChapter, on_delete=models.CASCADE)
    url = models.URLField( max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ('number', 'book',)

    def publish(self):
        self.save()

      



