from django.db import models
from django.utils import timezone


class Shelter(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.city}'


class Animal(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=1)
    arrival_date = models.DateField(default=timezone.now)
    weight = models.IntegerField(default=1)
    height = models.IntegerField(default=1)
    special_signs = models.TextField(default='subscribe....')
    is_arrived = models.BooleanField(default=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.shelter}, {self.is_arrived}'


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name, self.last_name}, {self.shelter}'
