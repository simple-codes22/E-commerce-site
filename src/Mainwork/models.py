from django.db import models
from django.urls import reverse
from datetime import date

class Store(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    user_name = models.CharField(max_length=30)
    e_Mail = models.EmailField()
    Amount = models.DecimalField(decimal_places=2, max_digits=10000)
    date_registered = models.DateField()
    password = models.CharField(max_length=30, unique=True)

    def __repr__(self):
        return f"User: {self.user_name}, ID: {self.id}"
