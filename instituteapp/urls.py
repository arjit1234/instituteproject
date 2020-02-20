from  django.urls import path
from instituteapp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('feedback/',views.feedback,name='feedback'),
    path('gallery/',views.gallery,name='gallery'),

]