from django.db import models

# Create your models here.

class District(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Mandal(models.Model):
    name=models.CharField(max_length=100)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Village(models.Model):
    name=models.CharField(max_length=100)
    mandal=models.ForeignKey(Mandal,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

