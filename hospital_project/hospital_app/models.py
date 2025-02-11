from django.db import models
from django.contrib.auth.models import User

'''A model is a blueprint for a database table. 
Defines the structure of the table, (columns and the type of data they store).'''

# Create your models here.

#Patient Table
class Patient(models.Model):
    PatientID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}" #Controls how the object is displayed as a string. Display patient as their full name
    
#Doctors Table
class Doctor(models.Model):
    DoctorID = models.AutoField(primary_key=True)
    DoctorName = models.CharField(max_length=100)
    Specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.DoctorName
        

#Appointments Table
class Appointment(models.Model):
    AppointmentID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE) #Deletes appointments when patient is deleted
    DoctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE) #
    AppointmentDate = models.DateField()
    Diagnosis = models.TextField()

    def __str__(self):
        return f"Appointment {self.AppointmentID}"
        
#Billing Table
class Billing(models.Model):
    BillID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE) #Deletes billing record when patient is deleted
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2) #Deletes appointments when doctor is deleted
    PaymentStatus = models.CharField(max_length=50)

    def __str__(self):
        return f"Bill {self.BillID}"
        
#Departments Table
class Department(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.DepartmentName

# DoctorDepartments Table
class DoctorDepartment(models.Model):
    DoctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    DepartmentID = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta: #Provides additional information about the DoctorDepartment Model class
        unique_together = ('DoctorID', 'DepartmentID') #Makes sure there are no duplicate Doctor-Department pairs

    def __str__(self):
        return f"Doctor {self.DoctorID} in Department {self.DepartmentID}"


'''Make migrations - This will create the database tables based on the models.
python manage.py makemigrations
python manage.py migrate'''

