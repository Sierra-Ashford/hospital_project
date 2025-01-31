from django import forms
from .models import Patient

class PatientForm(forms.ModelForm): #Automatically creates a form based on the model
    class Meta: #Defines model and fields used in the form
        model = Patient #Uses Patient model
        fields = ['FirstName', 'LastName', 'DateOfBirth'] 