from django.db import models

# Create your models here.
class Registration(models.Model):
    Name=models.CharField(max_length=154)
    Gender=models.CharField(max_length=20)
    Phone=models.CharField(max_length=12)
    Email=models.EmailField()
    Category=models.CharField(max_length=50,null=True,blank=True)
    Address=models.TextField()
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=100 )
    Age=models.IntegerField(null=True,blank=True)
    Dob=models.DateField(null=True,blank=True)
    #doctors

class Doctors(models.Model):
    Name=models.CharField(max_length=100)
    Dob=models.DateField()
    Gender=models.CharField(max_length=15)
    Phone=models.CharField(max_length=12)
    Age=models.IntegerField()
    Email=models.EmailField()
    Username=models.CharField(max_length=55)
    Address=models.TextField()
    Department=models.CharField(max_length=50)

    # Staffs

class Staffs(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Dob=models.DateField()
    Gender=models.CharField(max_length=20)
    Phone=models.CharField(max_length=12)
    Email=models.EmailField()
    Username=models.CharField(max_length=50)
    Address=models.TextField()
    Department=models.CharField(max_length=50)
    
    


    #  Patients
    
class Patients(models.Model):
    Username=models.CharField(max_length=50)
    Name=models.CharField(max_length=100)
    Phone=models.CharField(max_length=12)
    Age=models.IntegerField()
    Dob=models.DateField()
    Gender=models.CharField(max_length=20)
    Email=models.EmailField()
    Address=models.TextField()


    #Booking

class Booking(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    DOB=models.DateField()
    Gender=models.CharField(max_length=20,)
    Phone=models.CharField(max_length=12)
    Address=models.TextField()
    Email=models.EmailField()
    Appointment_Doctor=models.CharField(max_length=100)
    Appointment_Date=models.DateField()
    Appointment_Time=models.TimeField()
    Token=models.IntegerField(default=1)