from django.contrib import admin
from .models import Patient, Doctor, Appointment, Billing, Department, DoctorDepartment

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

"""Sample Queries for Django ORM(Object-Relational Mapper)"""
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


'''PostgreSQL
python manage.py dbshell
Check Tables- \dt'''



