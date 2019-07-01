from django.shortcuts import render,get_object_or_404
from .models import Course, Carrier, Event, Exam


def home(request):
    return render(request,'schoolapp/index.html', {})

def course(request):
    sub = Course.objects.all()
    return render(request, 'schoolapp/course.html', {'sub':sub})

def about(request):
    return render(request, 'schoolapp/about.html', {})

def contact(request):
    return render(request, 'schoolapp/contact.html', {})

def notification(request):
    carobj =Carrier.objects.all()
    evnt = Event.objects.all()
    exm = Exam.objects.all()
    return render(request, 'schoolapp/notification.html', {'carobj':carobj, 'evnt':evnt, 'exm':exm})
