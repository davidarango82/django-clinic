from django.urls import path

from . import views

app_name = "patients"
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    path('create/', views.PatientCreate.as_view(), name='patient_create'),
    ]