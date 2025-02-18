from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import DoctorViewSet, PatientViewSet, AppointmentViewSet, BillingViewSet, DepartmentViewSet
from . import views
from .views import (home, dashboard,
                    patient_list, patient_create, patient_detail, patient_update, patient_delete, 
                    add_doctor, doctor_list, update_doctor, delete_doctor,
                    appointment_list, appointment_create, appointment_detail, appointment_update, appointment_delete,
                    billing_list, billing_create, billing_detail, billing_update, billing_delete, 
                    department_list, department_create, department_detail, department_update, department_delete)

router = DefaultRouter() #Automatically generates URLs for viewsets
router.register(r'doctors', DoctorViewSet) #router.register: Registers viewsets under API routes
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'billing', BillingViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    #API Routes
    path('api/', include(router.urls)), #Includes all API routes

    #Template-Based Views for for dashboard and CRUD operations
    path('dashboard/', dashboard, name='dashboard'),
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

    #Billing CRUD URLs
    path('billing/', billing_list, name='billing_list'),
    path('billing/add/', billing_create, name='billing_create'),
    path('billing/<int:pk>/', billing_detail, name='billing_detail'),
    path('billing/<int:pk>/edit/', billing_update, name='billing_update'),
    path('billing/<int:pk>/delete/', billing_delete, name='billing_delete'),

    #Department CRUD URLs
    path('departments/', department_list, name='department_list'),
    path('departments/add/', department_create, name='department_create'),
    path('departments/<int:pk>/', department_detail, name='department_detail'),
    path('departments/<int:pk>/edit/', department_update, name='department_update'),
    path('departments/<int:pk>/delete/', department_delete, name='department_delete'),
]


'''
path(route, view, name): Defines a URL pattern
<int:pk> captures an integer (patient's ID) from the URL.
name='patient_list' allows us to reference this URL in templates
'''

'''Example
http://127.0.0.1:8000/patients/
'''
