from django.db import models
from django.utils import timezone
from .model_Account import Account

class UserSolicitud(models.Model):

    "Valores para los diferentes tipos de cuenta"
    alta='1'
    cambio='2'
    baja='4'
    AC_CHOICES= (
        (alta, 'alta'),
        (cambio, 'cambio'),
        (baja, 'baja')
    )
    free = 'f'
    normal = 'n'
    premium = 'p'
    TY_CHOICES= (
        (free, 'free'),
        (normal, 'normal'),
        (premium, 'premium')
    )
    "Valores del modelo"    
    """Si se pide una baja, se debe llenar con la fecha en que termina el plan.
        Si se pude el cambio, apenas empieza el dia de que termine el tiempo pagado del usuario,
        se debería cambiar el usuario al plan nuevo """

    """en caso de que el usuario quiera pagar tiempo hay que revisar que no tenga una solicitud de
      cambio de plan, en ese caso se debe generar una solicitud de alta con el plan nuevo y el tiempo"""  

    "tipo de solicitud que se hace"
    type_of_solicitud = models.CharField( max_length=2, choices=AC_CHOICES, default=alta)
    "tipo de plan al que se quiere cambiar, en caso de que sea baja, por defecto es free"
    type_of_plan = models.CharField( max_length=2, choices=TY_CHOICES, default=free)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_of_solicitud = models.DateTimeField(default=timezone.now)
    "fecha limite para atender la solicitud, si es un alta es un dia despues de la fecha de creacion"
    "si es un cambio o baja es cuando se termina el tiempo comprado por el usuario"
    date_limit_to_attend = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.type_of_solicitud