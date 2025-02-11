from django import forms
from .models import Patient, Doctor

class PatientForm(forms.ModelForm): #Automatically creates a form based on the model
    class Meta: #Defines model and fields used in the form
        model = Patient #Uses Patient model
        fields = ['FirstName', 'LastName', 'DateOfBirth'] 

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['DoctorName', 'Specialty']