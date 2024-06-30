from django.db import models

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=6)

    def __str__(self) -> str:
        return self.name
    
class Service(models.Model):
    type=models.CharField(max_length=50)
    modeOfPayment=models.CharField(max_length=50)
    company=models.CharField(max_length=100)
    subscriptions=models.ManyToManyField(User, related_name="services")

    def __str__(self) -> str:
        return self.type