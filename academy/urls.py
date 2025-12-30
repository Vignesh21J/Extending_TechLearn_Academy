from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.Courses, name="courses"),
    path('trainers/', views.Trainers, name="trainers"),
    path('students/', views.Students, name="students"),

    path('trainer/<int:pk>', views.Trainer_Detail, name="trainer-detail"),
    path('edit-trainer/<int:pk>', views.Update_Trainer, name="trainer-update"),
    path('delete-trainer/<int:pk>', views.Delete_Trainer, name='trainer-delete'),

    path('student/<int:pk>', views.Student_Detail, name="student-detail"),
    path('edit-student/<int:pk>', views.Update_Student, name="student-update"),
    path('delete-student/<int:pk>', views.Delete_Student, name="student-delete"),
    
]
