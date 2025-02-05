from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from .models import Patient
from .forms import PatientForm 
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

#List View - Show all patients, Only authenticated users can view patients
@login_required
def patient_list(request):
    patients = Patient.objects.all() #Gets all patients from the database
    return render(request, 'hospital_app/patient_list.html', {'patients': patients}) #Fills the HTML template with data

#Create View
@login_required
def patient_create(request):
    if request.method == "POST": #Checks if form is submitted
        form = PatientForm(request.POST) #Populate form with submitted data
        if form.is_valid(): #Ensures data is correct before saving
            form.instance.created_by = request.user #Associate patient with the user
            form.save() #Save new patient record
            return redirect('patient_list') #Redirect to patient list
    else:
        form = PatientForm() #Creates empty form
    return render(request, 'hospital_app/patient_form.html', {'form': form})
        
#Detail View
@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk) #Retrieves a patient or shows a 404 error if not found
    return render(request, 'hospital_app/patient_detail.html', {'patient': patient})

#Update View
@login_required
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.user != patient.created_by and not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission to edit this.")
    
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient) #Pre-fills the form with existing data
        if form.is_valid():
            form.save() #Saves updated record
            return redirect('patient_list') #Loads form with patient data
    else:
        form = PatientForm(instance=patient)
    return render(request, 'hospital_app/patient_form.html', {'form': form})

#Delete View
@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.user != patient.created_by and not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission to delete this.")
    
    patient.delete() #Deletes patient from database
    return redirect('patient_list') #Redirect to list view
    
