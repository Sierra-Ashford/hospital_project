from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Doctor, Patient, Appointment, Billing, Department
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, BillingSerializer, DepartmentSerializer
from .permissions import IsOwnerOrReadOnly

class DoctorViewSet(viewsets.ModelViewSet): #viewsets: DRF feature that simplifies CRUD operations and handles API requests
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]  #Only logged-in users can access the API
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['DoctorName', 'Specialty']  # Fields to search by, e.g., search by Doctor's name or specialty
    filterset_fields = ['Specialty']

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['FirstName', 'LastName']  # Search by patient's first name or last name
    filterset_fields = ['DateOfBirth', 'created_by']  # Filter by date of birth or the user who created the patient

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['Diagnosis', 'AppointmentDate']  # Search by diagnosis or appointment date
    filterset_fields = ['DoctorID', 'PatientID']  # Filter by doctor or patient

class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['PaymentStatus']  # Search by payment status
    filterset_fields = ['TotalAmount', 'PatientID']  # Filter by total amount or patient

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['DepartmentName', 'Description']  # Search by department name or description
    filterset_fields = ['DepartmentName']  # Filter by department name
