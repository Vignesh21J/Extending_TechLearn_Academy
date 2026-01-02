from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Trainer, Student

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth

from .forms import TrainerUpdateForm, StudentUpdateForm

from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def RegisterView(request):
    if request.user.is_authenticated:
        return redirect('home')

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
    if request.user.is_authenticated:
        return redirect('home')
    
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
    if not request.user.is_authenticated:
        return redirect('login')
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


@login_required
def Trainer_Detail(request, pk):
    # trainer = Trainer.objects.get(id=pk)
    
    trainer = get_object_or_404(Trainer, id=pk)
    context = {
        'trainer':trainer
    }

    return render(request, 'academy/trainer_detail.html', context)

@login_required
@permission_required('academy.change_trainer', raise_exception=True)
def Update_Trainer(request, pk):

    trainer = get_object_or_404(Trainer, id=pk)
    trainer_form = TrainerUpdateForm(instance=trainer)
    # print(form)
    
    if request.method == 'POST':
        form = TrainerUpdateForm(request.POST, request.FILES, instance=trainer)

        if form.is_valid():
            form.save()
            return redirect('trainers')
    else:
        form = TrainerUpdateForm(instance=trainer)

    context = {
        'trainer':trainer,
        'form':trainer_form
    }

    return render(request, 'academy/update_trainer.html', context)

@login_required
@permission_required('academy.delete_trainer', raise_exception=True)
def Delete_Trainer(request, pk):
    trainer = get_object_or_404(Trainer, id=pk)

    if request.method == 'POST':
        trainer.delete()
        return redirect('trainers')

    context = {
        'trainer': trainer
    }

    return render(request, 'academy/delete_trainer.html', context)


@login_required
@permission_required('academy.view_student', raise_exception=True)
def Student_Detail(request, pk):
    student = get_object_or_404(Student, id=pk)
    context = {
        'student':student
    }
    return render(request, 'academy/student_detail.html', context)

@login_required
@permission_required('academy.change_student', raise_exception=True)
def Update_Student(request, pk):
    student = get_object_or_404(Student, id=pk)
    student_form = StudentUpdateForm(instance=student)

    if request.method == 'POST':
        form = TrainerUpdateForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = TrainerUpdateForm(instance=student)

    context = {
        'student':student,
        'form':student_form
    }
    return render(request, 'academy/update_student.html', context)

@login_required
@permission_required('academy.delete_student', raise_exception=True)
def Delete_Student(request, pk):
    student = get_object_or_404(Student, id=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('students')

    context = {
        'student': student
    }

    return render(request, 'academy/delete_student.html', context)