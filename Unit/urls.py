from django.conf import settings
from django.urls import path
from . import views


# app_name = 'Unit'

urlpatterns = [
    path('', views.home, name='home' ),
    path('sign_up', views.sign_up, name='sign_up' ),
    path('studets_dashboard', views.StudentDash, name='StudentDash' ),
    path('teacher_dashboard', views.TeacherDash, name='teacherDash' ),
]

