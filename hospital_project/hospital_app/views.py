from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm 

# Create your views here.

#List View
def patient_list(request):
    patients = Patient.object.all()
    return render(request, 'hospital_app/patient_list.html', {'patients': patients})

#Create View
def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'hospital_app/patient_form.html', {'form': form})
        
#Detail View
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'hospital_app/patient_detail.html', {'patient': patient})

#Update View
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'hospital_app/patient_form.html', {'form': form})

#Delete View
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        patient.delete()
        return redirect('patient_list')
    return render(request, 'hospital_app/patient_confirm_delete.html', {'patient': patient})
