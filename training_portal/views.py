from django.shortcuts import render
from academy.models import Course, Trainer, Student

def Home(request):
    courses = Course.objects.count()

    trainers = Trainer.objects.count()

    students = Student.objects.count()

    context = {
        'courses_count':courses,
        'trainers_count':trainers,
        'students_count':students
    }
    return render(request, 'home.html', context)