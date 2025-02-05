from django.urls import path
from . import views
from .views import home

#Patient CRUD URLs
urlpatterns = [
    path('', home, name='home'),
    path('patients/', views.patient_list, name='patient_list'), #List all patients
    path('patients/create/', views.patient_create, name='patient_create'), #Create new patient
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'), #View patient details
    path('patients/<int:pk>/update/', views.patient_update, name='patient_update'), #Update patient info
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'), #Delete patient
]

'''
path(route, view, name): Defines a URL pattern
<int:pk> captures an integer (patient's ID) from the URL.
name='patient_list' allows us to reference this URL in templates
'''

'''Example
http://127.0.0.1:8000/patients/
'''
