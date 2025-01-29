from django.contrib import admin
from .models import Patient, Doctor, Appointment, Billing, Department, DoctorDepartment
# from django.apps import apps

#Create data models
'''Patient = apps.get_model('hospital_app', 'Patient')  
Appointment = apps.get_model('hospital_app', 'Appointment') 
Doctor = apps.get_model('hospital_app', 'Doctor')
Billing = apps.get_model('hospital_app', 'Billing')
Department = apps.get_model('hospital_app', 'Department')
DoctorDepartment = apps.get_model('hospital_app', 'DoctorDepartment')'''

'''apps.get_model
app label: The name of the app where the model is located. 
model name: The name of the model class you want to retrieve.'''

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Billing)
admin.site.register(Department)
admin.site.register(DoctorDepartment)
#Allows you to create, view, update, and delete records in your database tables through web interface.

'''Run the server
python manage.py runserver'''


'''Open Django shell to query data
python manage.py shell'''

"""Sample Querries"""
#Get all patients

'''from hospital_app.models import Patient
Patient.objects.all()'''

#Show Billing Information for All Patients

'''from hospital_app.models import Billing
for bill in Billing.objects.select_related('PatientID'):
    print(f"Bill ID: {bill.BillID}, Patient: {bill.PatientID.FirstName} {bill.PatientID.LastName}, "
          f"Total Amount: {bill.TotalAmount}, Payment Status: {bill.PaymentStatus}")'''

#List All Departments and Their Doctors

'''from hospital_app.models import DoctorDepartment
for record in DoctorDepartment.objects.select_related('DoctorID', 'DepartmentID'):
    print(f"Department: {record.DepartmentID.DepartmentName}, Doctor: {record.DoctorID.DoctorName}, "
          f"Specialty: {record.DoctorID.Specialty}")'''


