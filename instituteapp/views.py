from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'institute/home.html')

def contact(request):
    return  render(request,'institute/contact.html')

def services(request):
    return render(request,'institute/services.html')

def feedback(request):
    return render(request,'institute/feedback.html')

def gallery(request):
    return render(request,'institute/gallery.html')

