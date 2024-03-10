from django.shortcuts import render
from django.views import generic
from .models import Patient

class IndexView (generic.ListView): 
    template_name = "patients/index.html"
    context_object_name = "latest_patient_list" 
        
    def get_queryset(self): 
        """Return xxx""" 
        return Patient.objects.order_by ("lastname")[:5]
