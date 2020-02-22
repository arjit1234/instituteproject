from django.shortcuts import render
from .models import CourseData
# Create your views here.

def home(request):
    return render(request,'institute/home.html')

def contact(request):
    return  render(request,'institute/contact.html')

def services(request):

    courses=CourseData.objects.all()
    context={'course':courses}
    return render(request,'institute/services.html',context)

def feedback(request):
    return render(request,'institute/feedback.html')

def gallery(request):
    return render(request,'institute/gallery.html')

