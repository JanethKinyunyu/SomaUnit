from django.contrib import admin
from .models import Student, Course, Module, Teacher, Result 

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'enrolled_course', 'student_id']
    search_fields = ['first_name']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Module)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['score', 'result_type']