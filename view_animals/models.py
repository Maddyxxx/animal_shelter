from django.db import models
from django.utils import timezone


class Shelter(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}, {self.city}'


class Animal(models.Model):

    STATUS_CHOICES = (
        ('arrived', 'Arrived'),
        ('taken', 'Taken'),
    )
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=10)
    arrival_date = models.DateField(default=timezone.now)
    weight = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    special_signs = models.CharField(max_length=200, default='subscribe....')
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='arrived')
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.shelter}, {self.status}'


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name, self.last_name}, {self.shelter}'
