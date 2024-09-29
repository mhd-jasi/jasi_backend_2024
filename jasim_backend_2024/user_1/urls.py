from django.urls import path
from .import views

urlpatterns=[
    path('csrftoken',views.get_csrf_token,name='csrftoken'),
     path('Register',views.Register,name='Register'),
     path('login',views.login,name='login'),
     path('logout',views.logout,name='logout'),
     path('data_of_doctors',views.data_of_Doctors,name=' data of doctors'),
     path('data_of_staffs',views.data_of_Staffs,name='data_of_staff'),
     path('data_of_patients',views.data_of_Patients,name='data_of_patients'),
     path('display_data_of_Doctors',views.display_data_of_Doctors,name='display_data_of_Doctors'),
     path('display_data_of_Staffs',views.display_data_of_Staffs,name='display_data_of_Staffs'),
     path('display_data_of_Patients',views.display_data_of_Patients,name='display_data_of_Patients'),
     path('delete_data_of_person',views.delete_data_of_person,name='delete_data_of_person'),
     path('booking',views.booking,name='booking'),
     path('delete_booking',views.delete_booking,name='delete_booking'),
     path('search_for_doctors/',views.search_for_doctors, name='search_for_doctor'),
     path('search_for_staffs/',views.search_for_staffs,name='search_for_staffs'),
     path('search_for_patients/',views.search_for_patients,name='search_for_patients'),
]