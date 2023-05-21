from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about us/', views.about_us, name='about_us'),
    path('contact us/', views.contact_us, name='contact_us'),
    path('donation/', views.donation, name='donation'),
    path('medicate registration/', views.medicate_registration, name='medicate_registration'),
    path('medicine/', views.medicine, name='medicine'),
    path('Sign in/', views.Sign_in, name='Sign_in'),
]
