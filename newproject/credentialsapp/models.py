from django.db import models

# Create your models here.
class Practitioner(models.Model):
    first_name=models.CharField(max_length=255)   
    last_name=models.CharField(max_length=255)
    full_name=models.CharField(max_length=255)
    practice_name=models.CharField( max_length=255, null=True)
    notes=models.TextField(null=True)

    def __str__(self):
        return str(self.practice_name)

class Credential(models.Model):

    class CredentialType(models.TextChoices):
        INSURANCE ='Insurance'
        EMR   ='EMR'       
    type=models.CharField(max_length=50, choices=CredentialType.choices)
    system_name=models.CharField(max_length=30)  
    username=models.CharField(max_length=30) 
    password=models.CharField(max_length=30)
    notes=models.TextField(null=True) 
    practitioner=models.ForeignKey(Practitioner, on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.username) 


   