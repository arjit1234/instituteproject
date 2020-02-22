from  django.urls import path
from instituteapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('feedback/',views.feedback,name='feedback'),
    path('gallery/',views.gallery,name='gallery'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
