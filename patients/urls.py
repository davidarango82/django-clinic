
from django.urls import path

from . import views

#app_name = "patients"
urlpatterns = [
    
    path('', views.index, name='index'),
    path('list/', views.PatientListView.as_view(), name='patient-list'),
    path('<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('create/', views.PatientCreateView.as_view(), name='patient-create'),

    ]
