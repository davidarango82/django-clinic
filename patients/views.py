from django.shortcuts import render
from django.views import generic
from .models import Patient
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class IndexView (generic.ListView): 
    template_name = "patients/index.html"
    context_object_name = "latest_patient_list" 
        
    def get_queryset(self): 
        """Return xxx""" 
        return Patient.objects.order_by ("lastname")[:5]

class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    fields = '__all__'
    success_url = reverse_lazy('patients:all')