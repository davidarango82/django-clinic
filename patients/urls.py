
from django.urls import path

from . import views

#app_name = "patients"
urlpatterns = [
    
    path("", views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('create/', views.PatientCreateView.as_view(), name='patient_create'),

    ]
