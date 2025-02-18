from django import forms
from .models import Patient, Doctor, Appointment, Billing, Department

class PatientForm(forms.ModelForm): #Automatically creates a form based on the model
    class Meta: #Defines model and fields used in the form
        model = Patient #Uses Patient model
        fields = ['FirstName', 'LastName', 'DateOfBirth'] 

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['DoctorName', 'Specialty']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['PatientID', 'DoctorID', 'AppointmentDate', 'Diagnosis']
        widgets = {
            'AppointmentDate': forms.DateInput(attrs={'type': 'date'})
        }

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['PatientID', 'TotalAmount', 'PaymentStatus']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['DepartmentName', 'Description']
