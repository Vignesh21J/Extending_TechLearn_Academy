from django.shortcuts import render, redirect
from .models import Course, Trainer, Student

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth

# Create your views here.

def RegisterView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:    
        form = UserCreationForm()

    context = {'form':form}
        
    return render(request, 'accounts/register.html', context)


def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            user = form.get_user()
            # print(user)
            auth.login(request, user)
            return redirect('home')

    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def LogoutView(request):
    auth.logout(request)
    return redirect('login')

def Courses(request):
    courses = Course.objects.all()
    return render(request, 'academy/courses.html', {'courses':courses})

def Trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'academy/trainers.html', {'trainers':trainers})

def Students(request):
    students = Student.objects.all()
    return render(request, 'academy/students.html', {'students':students})