from django.db import models
from django.utils import timezone

""" En el UML se ve la clase KindOfDescription y sus tres herencias
Dado que la herencia era Total Exclusiva, se decidio eliminar el padre
y dejar solamente las tres clases hijo con los documentos repetidos """

"Futura mejora ->Declarar el Modelo KindOfDescription y generar relacion 1-1 con sus hijEs"
"Y asi no repetir codigo"
"Pero primero que funcione"

"----------------------------------------"
"Author"
"----------------------------------------"

class Author(models.Model):
    name= models.CharField("Nombre", max_length=50)
    last_name = models.CharField( max_length=50) 
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)


    def publish(self):
        self.save()

    def ret(sel):
        return self.name 
    def __str__(self):
        return self.name

"----------------------------------------"
" Gender"
"----------------------------------------"

class Gender(models.Model):
    name= models.CharField("Nombre", max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

"----------------------------------------"
" Editorial"
"----------------------------------------"

class Editorial(models.Model):
    name= models.CharField("Nombre", max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    mail = models.EmailField( max_length=254, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name