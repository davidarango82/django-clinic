from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth_date = models.DateTimeField("dd/mm/yyyy")
    pub_date = models.DateTimeField("date published")
    medical_record = models.CharField(max_length=20)
