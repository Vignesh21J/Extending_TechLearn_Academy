from django.shortcuts import render
from .models import Course, Trainer, Student

# Create your views here.
def Courses(request):
    courses = Course.objects.all()
    return render(request, 'academy/courses.html', {'courses':courses})

def Trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'academy/trainers.html', {'trainers':trainers})

def Students(request):
    students = Student.objects.all()
    return render(request, 'academy/students.html', {'students':students})