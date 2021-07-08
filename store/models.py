from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, CharField, DateTimeField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"

class manufacture(models.Model):
    id=models.AutoField(primary_key=True)
    name=CharField(max_length=64)
    address=CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class medicine(models.Model):
    mid=AutoField(primary_key=True)
    name=CharField(max_length=64)
    dosage=CharField(max_length=20)
    composition=CharField(max_length=64)
    stock=IntegerField()
    expiry=models.DateField()
    manu=ForeignKey(manufacture, on_delete=CASCADE, related_name="meds")
    price=FloatField(default=15)

    def __str__(self):
        return f"{self.name} {self.dosage}"

class patient(models.Model):
    pid=AutoField(primary_key=True)
    name=CharField(max_length=64)
    age=IntegerField()
    sex=CharField(max_length=6)
    phone=CharField(max_length=12)
    address=CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class bill(models.Model):
    billid=AutoField(primary_key=True)
    pid=ForeignKey(patient, on_delete=CASCADE, related_name="patient")
    time=DateTimeField(auto_now_add=True)
    total=FloatField(default=0.0)

    def __str__(self):
        return f"{self.billid} at {self.time}"

class buy(models.Model):
    billid=ForeignKey(bill, on_delete=CASCADE, related_name="bill")
    mid=ForeignKey(medicine, on_delete=CASCADE, related_name="patients")
    qty=IntegerField()
    cost=FloatField()

    def __str__(self):
        return f"{self.billid}"