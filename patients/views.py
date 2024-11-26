from django.shortcuts import render
from .models import Patient
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    """View function for home page of site."""
    # Generate count of some of patients
    num_patients = Patient.objects.all().count()

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_patients': num_patients, },
    )

#def index (request): 
#    template_name = "patients/index.html"

#    def get_queryset(self): 
#        """Return xxx""" 
#        return Patient.objects.order_by ("lastname")[:5]

class PatientListView(ListView):
    model = Patient

class PatientDetailView(DetailView):
    model = Patient

class PatientCreateView(CreateView):
    model = Patient
    fields = '__all__'
    success_url = reverse_lazy('patients:index')
