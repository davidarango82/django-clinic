from django.db import models

class Patient(models.Model):
    medical_record = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    DNI = models.CharField(max_length=20)
    birth_date = models.DateField("Birth Date (YYYY-MM-DD)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)