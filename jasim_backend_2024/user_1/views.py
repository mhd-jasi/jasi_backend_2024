#from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json

from .models import Registration,Doctors,Patients,Staffs,Booking
from django.contrib.auth.hashers import make_password,check_password
from django.views.decorators.csrf import csrf_exempt
#from .serializer import serialize_doctors_data,serialize_patients_data
from django.middleware.csrf import get_token
from django.contrib.auth import logout
from django.db.models import Q

 #Create your views here.
def serialize_patients_data(queryset):
    return[
        {
            'id':obj.id,
            'Username':obj.Username,
            'Name':obj.Name,
            'Phone':obj.Phone,
            'Age':obj.Age,
            'Dob':obj.Dob,
            'Gender':obj.Gender,
            'Email':obj.Email,
            'Address':obj.Address
        }
        for obj in queryset
    ]

def serialize_doctors_data(queryset):
    return[
        {
            'id':obj.id,
            'Name':obj.Name,
            'Dob':obj.Dob,
            'Gender':obj.Gender,
            'Phone':obj.Phone,
            'Age':obj.Age,
            'Email':obj.Email,
            'Username':obj.Username,
            'Address':obj.Address,
            'Department':obj.Department
        }
        for obj in queryset
    ]

def serialize_staffs_data(queryset):
    return[
        {
            'id':obj.id,
            'Name':obj.Name,
            'Age':obj.Age,
            'Dob':obj.Dob,
            'Gender':obj.Gender,
            'Phone':obj.Phone,
            'Email':obj.Email,
            'Username':obj.Username,
            'Address':obj.Address,
            'Department':obj.Department


        }
        for obj in queryset
    ]

def get_csrf_token(request):
    csrf_token=get_token(request)
    return JsonResponse({"csrftoken":csrf_token})

@csrf_exempt
def Register(request):
    if request.method=='POST':
        name=request.POST.get('NAME')
        gender=request.POST.get('GENDER')
        phone=request.POST.get('PHONE')
        email=request.POST.get('EMAIL')
        category=request.POST.get('CATEGORY')
        address=request.POST.get('ADDRESS')
        username=request.POST.get('USERNAME')
        age=request.POST.get('AGE')
        dob=request.POST.get('DOB')
        password=request.POST.get('PASSWORD')
        

        if Registration.objects.filter(Username=username).exists():
            return JsonResponse({'error':'The username is already taken'})
        else:
            if category=='Doctor':
                Doctors.objects.create(Name=name,Gender=gender,Phone=phone,Email=email,Address=address,Username=username,Age=age,Dob=dob)
                Registration.objects.create(Name=name,Gender=gender,Phone=phone,Email=email,Address=address,Username=username,Age=age,Dob=dob,
                                            Password=make_password(password),Category=category)

            elif category=='Patients' :
                 Patients.objects.create(Name=name,Gender=gender,Phone=phone,Email=email,Address=address,Username=username,Age=age,Dob=dob)
                 Registration.objects.create(Name=name,Gender=gender,Phone=phone,Email=email,Address=address,Username=username,Age=age,Dob=dob,
                                             Password=make_password(password),Category=category)

            else:
                Staffs.objects.create(Name=name,Gender=gender,Phone=phone,Email=email,Address=address,Username=username,Age=age,Dob=dob)
                Registration.objects.create(Name=name,Gender=gender,Phone=phone,Email=email,Address=address,Username=username,Age=age,Dob=dob,
                                             Password=make_password(password),Category=category)
            
            return JsonResponse({"success":"Your Registration completed"})
    else:
        return JsonResponse({"error":"the method is wrong"})

@csrf_exempt
def login(request):
   
    if request.method=='POST':
        username=request.POST.get('USERNAME')
        password=request.POST.get('PASSWORD')

        if request.session.get('user_id'):

            return JsonResponse({
                'message':'User already logged in',
                'status':'success',
                'username': request.session.get('PHONE')
            })
        
        if Registration.objects.filter(Username=username).exists():
            data=Registration.objects.get(Username=username)

            if data.Username==username and check_password(password,data.Password):
                respones= JsonResponse({'success':'login successfully'})
                respones.set_cookie('login_cookie','cookie_value',max_age=3600)

                request.session['username']=data.Username
                request.session['user_id']=data.id

                csrf_token=get_token(request)
                respones.set_cookie('csrftoken',csrf_token)

                return respones
            else:
                 return JsonResponse({'error':'password is wrong'})
        else:
            return JsonResponse({'error':'username not found' })
    else:
        return JsonResponse({'error':'the method is wrong'})
    
@csrf_exempt
def logout(request):
    
    logout(request)
    response= JsonResponse({'message':'logout successfully'})
    response.delete_cookie('login_cookie')
    response.delete_cookie('csrftoken')
    

    return response
    
@csrf_exempt
def data_of_Doctors(request):
    if request.method=="POST":
        username=request.POST.get('USERNAME')
        phone=request.POST.get('PHONE')
        email=request.POST.get('EMAIL')
        address=request.POST.get('ADDRESS')
        department=request.POST.get('DEPT')
        age=request.POST.get('AGE')
        dob=request.POST.get('DOB')
        gender=request.POST.get('GENDER')


        if Doctors.objects.filter(Username=username).exists():
           data= Doctors.objects.get(Username=username)
           datas=Registration.objects.get(Username=username)
           data.Phone=datas.Phone=phone
           data.Email=datas.Email=email
           data.Address=datas.Address=address
           data.Department=department
           data.Age=age
           data.Dob=dob
           data.Gender=gender
           data.save()
           datas.save()

           return JsonResponse({'success':'data entry successfully'})
        else:
            return JsonResponse({'error':'user not found , try after Registration'})
    
    else:
        return JsonResponse({'error':'method is wrong'})
        
@csrf_exempt
def data_of_Staffs(request):
    if request.method=="POST":
        username=request.POST.get('USERNAME')
        phone=request.POST.get('PHONE')
        email=request.POST.get('EMAIL')
        address=request.POST.get('ADDRESS')
        department=request.POST.get('DEPT')
        age=request.POST.get('AGE')
        dob=request.POST.get('DOB')
        gender=request.POST.get('GENDER')

        if Staffs.objects.filter(Username=username).exists():
           data=Staffs.objects.get(Username=username)
           datas=Registration.objects.get(Username=username)
           data.Phone=datas.Phone=phone
           data.Email=datas.Email=email
           data.Address=datas.Address=address
           data.Department=department
           data.Age=age
           data.Dob=dob
           data.Gender=gender
           data.save()
           datas.save()

           return JsonResponse({'success':'data entry successfully'})
        else:
            return JsonResponse({'error':'user not found , try after Registration'})
    
    else:
        return JsonResponse({'error':'method is wrong'})
        
@csrf_exempt
def data_of_Patients(request):
    if request.method=="POST":
       username=request.POST.get('USERNAME')
       Phone=request.POST.get('PHONE')
       email=request.POST.get('EMAIL')
       address=request.POST.get('ADDRESS')
       age=request.POST.get('AGE')
       dob=request.POST.get('DOB')
       gender=request.POST.get('GENDER')

       if Patients.objects.filter(Username=username).exists():
           data=Patients.objects.get(Username=username)
           datas=Registration.objects.get(Username=username)
           data.Phone=datas.Phone=Phone
           data.Email=datas.Email=email
           data.Address=datas.Address=address
           data.Age=age
           data.Dob=dob
           data.Gender=gender
           data.save()
           datas.save()
       
           return JsonResponse({'success':'patient data entry successfully'})
      
       else:
           return JsonResponse({'error':'user not found, try after registrations'})
    else:
        return JsonResponse({'error':'method is wrong'})

@csrf_exempt

def booking(request):
    if request.method=='POST':
        name=request.POST.get('NAME')
        age=request.POST.get('AGE')
        dob=request.POST.get('DOB')
        gender=request.POST.get('GENDER')
        phone=request.POST.get('PHONE')
        address=request.POST.get('ADDRESS')
        email=request.POST.get('EMAIL')
        doctor=request.POST.get('DOCTOR')
        date=request.POST.get('DATE')
        time=request.POST.get('TIME')
        
        
        if Booking.objects.filter(Name=name).exists():
            return JsonResponse({'error':"your are aleady booked"})
        
        else:
           try:
               last_token=Booking.objects.all().order_by('Token').last()
               new_token=last_token.Token+1

               Booking.objects.create(Name=name,Age=age,DOB=dob,Phone=phone,Address=address,Email=email,
                               Appointment_Doctor=doctor,Appointment_Date=date,Appointment_Time=time,
                               Gender=gender,Token=new_token)  
        
               return JsonResponse({'success':'your booking successfully',
                                 'Appointment_Doctor':doctor,
                                 'Appointment_Date':date, 
                                 'Appointment_Time':time ,
                                 'Token number is':new_token})
  
            
           except:
               
               Booking.objects.create(Name=name,Age=age,DOB=dob,Phone=phone,Address=address,Email=email,
                               Appointment_Doctor=doctor,Appointment_Date=date,Appointment_Time=time,
                               Gender=gender)  
               return JsonResponse({'success':'your booking successfully',
                                 'Appointment_Doctor':doctor,
                                 'Appointment_Date':date, 
                                 'Appointment_Time':time ,
                                 'Token number is':new_token})
               

    
    
    else:
      return JsonResponse({'error':'The method is wrong'})

@csrf_exempt
def delete_booking(request):
    if request.method=='POST':
     phone=request.POST.get('phone')

    if Booking.objects.filter(Phone=phone).exists():
        Booking.objects.get(Phone=phone).delete()
        return JsonResponse({'success':"The booking has been deleted"})
    else:
        return JsonResponse({'error':'you have no booking'})

@csrf_exempt 
def delete_data_of_person(request):
    if request.method=='POST':
        username=request.POST.get('username')

        if Registration.objects.filter(Username=username).exists():
           data= Registration.objects.get(Username=username)
           datas=data.Category

           if datas=='Doctor':
               Doctors.objects.get(Username=username).delete()
               Registration.objects.get(Username=username).delete()

               return JsonResponse({'status':'successfully delete all datas of the Doctor'})
           
           elif datas=='Patients':
               Patients.objects.get(Username=username).delete()
               Registration.objects.get(Username=username).delete()
               
               return JsonResponse({'status':'successfully delete all datas of the Patient'})
           else:
               Staffs.objects.get(Username=username).delete()
               Registration.objects.get(Username=username).delete()

               return JsonResponse({'status':'successfully delete all datas of the Staff'})
        else:
           return JsonResponse({'error':'user not found'})


           


      

@csrf_exempt
def display_data_of_Doctors(request):
    
        
         username=request.POST.get('username')
         
         if Doctors.objects.filter(Username=username).exists():
             data=Doctors.objects.filter(Username=username)
             data1=serialize_doctors_data(data)
             return JsonResponse(data1,safe=False)

         else:
             return JsonResponse({'error':'User not found'})

@csrf_exempt
def display_data_of_Staffs(request):
        
         username=request.POST.get('username')
         
         if Staffs.objects.filter(Username=username).exists():
             data=Staffs.objects.filter(Username=username)   
             data1=serialize_staffs_data(data)
             return JsonResponse(data1,safe=False)
       
         else:
             return JsonResponse({'error':'User not found'})


@csrf_exempt
def display_data_of_Patients(request):
        
         username=request.POST.get('username')
         
         if Patients.objects.filter(Username=username).exists():
             data=Patients.objects.filter(Username=username)
             data1=serialize_patients_data(data)
             return JsonResponse(data1,safe=False)      
       
         else:
             return JsonResponse({'error':'User not found'})

          





def search_for_doctors(request):
    name = request.GET.get('name', '')  
    if name:
        data = Doctors.objects.filter(Name__icontains=name) | Doctors.objects.filter(Email__icontains=name)
        data1 = serialize_doctors_data(data)
        return JsonResponse({'status':'success','data':data1},safe=False)
    else:
        return JsonResponse({'error': "no user found"})  





@csrf_exempt
def search_for_staffs(request):
    name = request.GET.get('name', '') 
    if name :
        data= Staffs.objects.filter(Name__icontains=name) | Staffs.objects.filter(Phone__icontains=name)
        data1 = serialize_staffs_data(data)
        return JsonResponse({'status':'success','data':data1},safe=False)
    else:
        return JsonResponse({'error':"no user found"})


@csrf_exempt
def search_for_patients(request):
    name = request.GET.get('name', '') 
    if name :
        data=Patients.objects.filter(Name__icontains=name) | Patients.objects.filter(Phone__icontains=name)
        data1 = serialize_patients_data(data)
        return JsonResponse({'status':'success','data':data1},safe=False)
    else:
        return JsonResponse({'error':"no user found"})



