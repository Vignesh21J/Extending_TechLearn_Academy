from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    duration = models.IntegerField(verbose_name='Duration (in weeks)')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Trainer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    expertise = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    enrolled_course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"