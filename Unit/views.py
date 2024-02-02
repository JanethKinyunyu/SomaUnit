from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import StudentRegistrationForm, TeacherRegistrationForm, StudentAuthenticationForm, TeacherAuthenticationForm

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # the dashboard view
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_registration.html', {'form': form})

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
                return redirect('dashboard')  # the dashboard view
    else:
        form = StudentAuthenticationForm()
    return render(request, 'student_login.html', {'form': form})

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