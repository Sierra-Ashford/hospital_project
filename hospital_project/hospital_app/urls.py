from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import DoctorViewSet, PatientViewSet, AppointmentViewSet, BillingViewSet, DepartmentViewSet
from . import views
from .views import (home, dashboard,
                    patient_list, patient_create, patient_detail, patient_update, patient_delete, 
                    add_doctor, doctor_list, update_doctor, delete_doctor,
                    appointment_list, appointment_create, appointment_detail, appointment_update, appointment_delete)

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'billing', BillingViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    #API Routes
    path('api/', include(router.urls)),

    #Template-Based Views
    path('', dashboard, name='dashboard'),
    path('home/', home, name='home'),

    #Patient CRUD URLs
    path('patients/', patient_list, name='patient_list'), #List all patients
    path('create/', patient_create, name='patient_create'), #Create new patient
    path('<int:pk>/', patient_detail, name='patient_detail'), #View patient details
    path('<int:pk>/update/', patient_update, name='patient_update'), #Update patient info
    path('<int:pk>/delete/', patient_delete, name='patient_delete'), #Delete patient

    #Doctor CRUD URLs
    path('doctors/', doctor_list, name='doctor_list'),
    path('doctors/add/', add_doctor, name='add_doctor'),
    path('doctors/edit/<int:doctor_id>/', update_doctor, name='update_doctor'),
    path('doctors/delete/<int:doctor_id>/', delete_doctor, name='delete_doctor'),

    #Apointment CRUD URLs
    path('appointments/', appointment_list, name='appointment_list'),
    path('appointments/add/', appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/', appointment_detail, name='appointment_detail'),
    path('appointments/<int:pk>/edit/', appointment_update, name='appointment_update'),
    path('appointments/<int:pk>/delete/', appointment_delete, name='appointment_delete'),
]


'''
path(route, view, name): Defines a URL pattern
<int:pk> captures an integer (patient's ID) from the URL.
name='patient_list' allows us to reference this URL in templates
'''

'''Example
http://127.0.0.1:8000/patients/
'''
