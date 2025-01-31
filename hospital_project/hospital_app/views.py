from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm 

# Create your views here.

#List View - Show all patients
def patient_list(request):
    patients = Patient.objects.all() #Gets all patients from the database
    return render(request, 'hospital_app/patient_list.html', {'patients': patients}) #Fills the HTML template with data

#Create View
def patient_create(request):
    if request.method == "POST": #Checks if form is submitted
        form = PatientForm(request.POST) #Populate form with submitted data
        if form.is_valid(): #Ensures data is correct before saving
            form.save() #Save new patient record
            return redirect('patient_list') #Redirect to patient list
    else:
        form = PatientForm() #Creates empty form
    return render(request, 'hospital_app/patient_form.html', {'form': form})
        
#Detail View
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk) #Retrieves a patient or shows a 404 error if not found
    return render(request, 'hospital_app/patient_detail.html', {'patient': patient})

#Update View
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient) #Pre-fills the form with existing data
        if form.is_valid():
            form.save() #Saves updated record
            return redirect('patient_list') #Loads form with patient data
    else:
        form = PatientForm(instance=patient)
    return render(request, 'hospital_app/patient_form.html', {'form': form})

#Delete View
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST": #POST is used to prevent accidental deletions.
        patient.delete() #Deletes patient from database
        return redirect('patient_list') #Redirect to list view
    return render(request, 'hospital_app/patient_confirm_delete.html', {'patient': patient})
