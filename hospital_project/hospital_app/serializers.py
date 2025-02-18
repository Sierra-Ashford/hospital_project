from rest_framework import serializers
from .models import Doctor, Patient, Appointment, Billing, Department

class DoctorSerializer(serializers.ModelSerializer): #ModelSerializer: Auto-generates fields from the Doctor model
    class Meta: #Specifies the model and includes all fields
        model = Doctor
        fields = '__all__'  

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

#Each serializer converts the model into JSON for API responses

