from django.db import models
from django.utils import timezone
from .model_CreditCards import CreditCards


"En el UML Account tenia diferentes herencias, como estas podian ir cambiando durante el tiempo"
"Se decidio dejar solo la clase padre"

class Account(models.Model):
    "Valores para los diferentes tipos de cuenta"
    free='1'
    normal='2'
    premium='4'
    admin = '9'
    AC_CHOICES= (
        (free, 'free'),
        (normal, 'normal'),
        (premium, 'premium'),
        (admin, 'admin')
    )
    "Valores del modelo"
    email = models.EmailField(max_length=254, unique=True, )
    user_name = models.CharField(max_length=50,primary_key=True )
    password= models.CharField(max_length=70, )
    plan = models.CharField( max_length=2, choices=AC_CHOICES, default=free)
    date_start_plan = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    time_pay = models.IntegerField(default=0)
    card = models.OneToOneField(CreditCards, on_delete=models.CASCADE)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.user_name

