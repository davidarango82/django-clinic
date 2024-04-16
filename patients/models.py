from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    NIF = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField(help_text="(YYYY-MM-DD)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #medical_record = models.CharField(max_length=20) #possibly for future use. Relationship w/ CRM/ERP