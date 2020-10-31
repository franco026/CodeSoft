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

    person = (
        ('medical', 'Doctor'),
        ('patient', 'Paciente')
    )
    document_type = models.CharField(max_length = 50, choices=types)
    document_number = models.IntegerField(null = True)
    year_old = models.IntegerField(null = True)
    phone = models.IntegerField(null = True)
    is_connected = models.BooleanField(default=True)
    user_type = models.CharField(choices=person, max_length=9, default='Paciente')

    def __str__(self):
        return '{0},{1}'.format(self.first_name, self.last_name)

    

class patient(models.Model):
    disease_status = (
        ('N', 'Neutro'),
        ('+', 'Positivo'),
        ('-', 'Negativo'),
        ('F', 'Fallecido'),
    )
    idPaciente = models.OneToOneField(User,null = True,blank = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    patient_status = models.CharField(max_length = 1, choices=disease_status,default='Positivo')
    location = models.TextField()

class medical(models.Model):
    idDoctor =  models.OneToOneField(User,null = True,blank = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)