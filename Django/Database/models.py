from django.db import models
from django.utils import timezone


# Create your models here.

class Client(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    birthdate = models.DateField(blank=True)
    address = models.CharField(max_length=254, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    vaccinated = models.BooleanField()
    photo_preference = models.BooleanField()
    emergency_contact = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return f"{self.first} {self.last}"


class Course(models.Model):
    name = models.CharField(max_length=200)
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    instructor = models.CharField(max_length=200, blank=True)
    resident_cost = models.IntegerField(blank=True)
    non_resident_cost = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.name}"


class SignIn(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.client.first

