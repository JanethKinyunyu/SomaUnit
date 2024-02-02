from django.conf import settings
from django.urls import path
from . import views


# app_name = 'Unit'

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_up', views.student_registration, name='sign_up'),
    path('sign_in', views.student_login, name='sign_in'),
    path('dashboards', views.dashboards, name='dashboards'),
    path('logout', views.logout, name='logout'),
    # path('studets_dashboard', views.StudentDash, name='StudentDash' ),
    # path('teacher_dashboard', views.TeacherDash, name='teacherDash' ),
]


