from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    types = (
        ('CI', 'cédula de identidad'),
        ('CC', 'cédula de ciudadanía '),
        ('TI', 'tarjeta de identidad'),
        ('TP', 'tarjeta pasaporte'),
        ('RC', 'registro civil'),
        ('CE', 'cédula de extranjería'),
    )
    document_type = models.CharField(max_length = 50, choices=types)
    document_number = models.IntegerField(null = True)
    year_old = models.IntegerField(null = True)
    phone = models.IntegerField(null = True)
    is_connected = models.BooleanField(default=True)
    
    

class medical(User):
    
    def __str__(self):
        return '{0},{1}'.format(self.first_name, self.last_name)

class patient(User):
    disease_status = (
        ('N', 'Neutro'),
        ('+', 'Positivo'),
        ('-', 'Negativo'),
        ('F', 'Fallecido'),
    )
    doctores = models.ForeignKey(medical, related_name='pacientes', on_delete=models.CASCADE)
    patient_status = models.CharField(max_length = 15, choices=disease_status,default='Positivo')
    location = models.TextField()

