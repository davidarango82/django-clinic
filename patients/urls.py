
from django.urls import path

from . import views

#app_name = "patients"
urlpatterns = [
    
    path("", views.IndexView.as_view(), name="index"),
    path('create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('patient/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),
    ]