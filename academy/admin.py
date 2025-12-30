from django.contrib import admin
from .models import Course, Trainer, Student

# Register your models here.
# admin.site.register(Course)
# admin.site.register(Trainer)
# admin.site.register(Student)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'duration']
    search_fields = ['name', 'description']
    ordering = ['-id']
admin.site.register(Course, CourseAdmin)


class TrainerAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name','expertise']
    list_filter = ['expertise']
    search_fields = ['first_name', 'last_name', 'email']
    list_display_links = ['full_name']
    ordering = ["-id"]
admin.site.register(Trainer, TrainerAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name','email', 'enrolled_course', 'trainer', 'is_active']
    list_filter = ['enrolled_course', 'trainer']
    search_fields = ['first_name', 'last_name', 'email']
    list_editable = ['is_active']
    list_display_links = ['full_name', 'email']
    ordering = ["-id"]
admin.site.register(Student, StudentAdmin)