from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .models import Patient, Doctor, Appointment, Billing, Department
from .forms import PatientForm, DoctorForm, AppointmentForm, BillingForm, DepartmentForm


# Create your views here.

# Function to check if user is NOT in PatientManager group
def is_not_patient_manager(user):
    return not user.groups.filter(name="PatientManager").exists()

#Dashboard View
def dashboard(request):
    return render(request, 'hospital_app/dashboard.html')

#Homepage
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
@login_required #Only allows authorized users to update patients.
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
@login_required #Requires permission to delete patient records 
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.user != patient.created_by and not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission to delete this.")
    
    patient.delete() #Deletes patient from database
    return redirect('patient_list') #Redirect to list view

#Doctor Views (Restricted for Reception)
@login_required
@user_passes_test(is_not_patient_manager)
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')  # Redirect to list of doctors
    else:
        form = DoctorForm()
    return render(request, 'hospital_app/doctor_form.html', {'form': form})

@login_required
@user_passes_test(is_not_patient_manager, login_url='/')
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospital_app/doctor_list.html', {'doctors': doctors})

@login_required
@user_passes_test(is_not_patient_manager)
def update_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, DoctorID=doctor_id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'hospital_app/doctor_form.html', {'form': form})

@login_required
@user_passes_test(is_not_patient_manager)
def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, DoctorID=doctor_id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'hospital_app/doctor_confirm_delete.html', {'doctor': doctor})


#Appointment View
@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'hospital_app/appointment_list.html', {'appointments': appointments})

@login_required
def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')  # Redirect to list of appointments
    else:
        form = AppointmentForm()
    return render(request, 'hospital_app/appointment_form.html', {'form': form})

@login_required
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, AppointmentID=pk)
    return render(request, 'hospital_app/appointment_detail.html', {'appointment': appointment})

@login_required
def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, AppointmentID=pk)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'hospital_app/appointment_form.html', {'form': form})

@login_required
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, AppointmentID=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'hospital_app/appointment_confirm_delete.html', {'appointment': appointment})

#Billing Views
@login_required
def billing_list(request):
    billings = Billing.objects.all()
    return render(request, 'hospital_app/billing_list.html', {'billings': billings})

@login_required
def billing_create(request):
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('billing_list')
    else:
        form = BillingForm()
    return render(request, 'hospital_app/billing_form.html', {'form': form})

@login_required
def billing_detail(request, pk):
    billing = get_object_or_404(Billing, BillID=pk)
    return render(request, 'hospital_app/billing_detail.html', {'billing': billing})

@login_required
def billing_update(request, pk):
    billing = get_object_or_404(Billing, BillID=pk)
    if request.method == "POST":
        form = BillingForm(request.POST, instance=billing)
        if form.is_valid():
            form.save()
            return redirect('billing_list')
    else:
        form = BillingForm(instance=billing)
    return render(request, 'hospital_app/billing_form.html', {'form': form})

@login_required
def billing_delete(request, pk):
    billing = get_object_or_404(Billing, BillID=pk)
    if request.method == 'POST':
        billing.delete()
        return redirect('billing_list')
    return render(request, 'hospital_app/billing_confirm_delete.html', {'billing': billing})

#Department Views (Restricted for Reception)
@login_required
@user_passes_test(is_not_patient_manager, login_url='/')
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'hospital_app/department_list.html', {'departments': departments})

@login_required
@user_passes_test(is_not_patient_manager)
def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'hospital_app/department_form.html', {'form': form})

@login_required
@user_passes_test(is_not_patient_manager)
def department_detail(request, pk):
    department = get_object_or_404(Department, DepartmentID=pk)
    return render(request, 'hospital_app/department_detail.html', {'department': department})

@login_required
@user_passes_test(is_not_patient_manager)
def department_update(request, pk):
    department = get_object_or_404(Department, DepartmentID=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'hospital_app/department_form.html', {'form': form})

@login_required
@user_passes_test(is_not_patient_manager)
def department_delete(request, pk):
    department = get_object_or_404(Department, DepartmentID=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'hospital_app/department_confirm_delete.html', {'department': department})
