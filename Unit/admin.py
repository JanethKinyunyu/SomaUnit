from django.contrib import admin
from .models import Student, Course, Module, Teacher, Result 

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id']
    search_fields = ['studemt_id']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']