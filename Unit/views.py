from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm, TeacherRegistrationForm, StudentAuthenticationForm, TeacherAuthenticationForm
from .models import Student, Teacher, Course, Module

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # the dashboard view
    else:
        form = StudentRegistrationForm()
    return render(request, 'SomaUnit/signup.html', {'form': form})

def teacher_registration(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # the dashboard view
    else:
        form = TeacherRegistrationForm()
    return render(request, 'teacher_registration.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        form = StudentAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('StudentDash')  # the dashboard view
    else:
        form = StudentAuthenticationForm()
    return render(request, 'SomaUnit/dashboards/Student_dashboard.html', {'form': form})

def teacher_login(request):
    if request.method == 'POST':
        form = TeacherAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')  # the dashboard view
    else:
        form = TeacherAuthenticationForm()
    return render(request, 'teacher_login.html', {'form': form})


def home(request):
    return render(request, 'index.html')


def sign_up(request):
    return render(request, 'SomaUnit/signup.html')

def sign_in(request):
    return render(request, 'SomaUnit/signin.html')


@login_required
def dashboards(request):
    user = request.user

    if hasattr(user, 'is_student'):
        student = user.student
        return render(request, 'SomaUnit/dashboards/student_dashboard.html', {'student': student})
    elif hasattr(user, 'is_teacher'):
        teacher = user.teacher
        return render(request, 'SomaUnit/dashboards/teacher_dashboard.html', {'teacher': teacher})
    else:
        return render(request, 'SomaUnit/signin.html', {'error_message': 'Invalid user type'})


def student_dashboard(request):
    student = Student.objects.all()
    return render(request, 'SomaUnit/dashboards/Student_dashboard.html', {'student', student})

@login_required
def Custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully! ")
    return redirect('home')
