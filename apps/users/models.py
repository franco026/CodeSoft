from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 100)
    typedocument = models.CharField(max_length = 50)
    numberdocument = models.IntegerField(null = True)
    year_old = models.IntegerField(null = True)
    phone = models.IntegerField(null = True)
    email = models.EmailField()
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 100)
    is_active = models.BooleanField(default=True)
    is_medical = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.fullname)


class patient(models.Model):
    idPaciente = models.OneToOneField(Users,null = True,blank = True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)
    disease = models.CharField(max_length = 20)
    location = models.TextField()

class medical(models.Model):
    idDoctor =  models.OneToOneField(Users,null = True,blank = True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)