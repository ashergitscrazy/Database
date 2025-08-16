from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.

class Client(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    birthdate = models.DateField()
    street1 = models.CharField(max_length=254, default="")
    street2 = models.CharField(max_length=254, default="")
    city = models.CharField(max_length=254, default="")
    state = models.CharField(max_length=2, default="")
    zip = models.CharField(max_length=10, default="")
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    vaccinated = models.BooleanField()
    photo_preference = models.BooleanField()
    emergency_contact1 = models.CharField(max_length=200, default="")
    emergency_phone1 = models.CharField(max_length=10, default="")
    emergency_contact2 = models.CharField(max_length=200, default="")
    emergency_phone2 = models.CharField(max_length=10, default="")
    emt_info = models.CharField(max_length=1000, default="")
    is_resident = models.BooleanField(default=False)

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
    resident_cost = models.FloatField(null=True, blank=True, default=0.0)
    non_resident_cost = models.FloatField(null=True, blank=True, default=0.0)
    set_date = models.DateTimeField(null=True, blank=True, default=datetime.strptime("2001-01-01", "%Y-%m-%d"))

    def __str__(self):
        return f"{self.name}"


class SignIn(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.client.first


class SheetImport(models.Model):
    sheet_url = models.URLField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    def __str__(self):
        return self.sheet_url
