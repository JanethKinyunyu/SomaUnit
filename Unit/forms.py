from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Teacher, Course

class StudentRegistrationForm(UserCreationForm):
    # pass
    class Meta:
        model = User
        fields = ['username', 'first_name', 'middle_name', 'last_name', 'is_student', 'enrolled_course', 'password1', 'password2']

    first_name = forms.CharField(max_length=255)
    middle_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    enrolled_course = forms.ModelChoiceField(queryset=Course.objects.all())  # Adjust the queryset accordingly
    is_student = forms.BooleanField(initial=True, widget=forms.HiddenInput(), required=False)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.last_login = None       
        user.save()
        student = Student.objects.create(user=user, first_name=self.cleaned_data['first_name'] ,middle_name=self.cleaned_data['middle_name'], last_name=self.cleaned_data['last_name'], enrolled_course=self.cleaned_data['enrolled_course'])
        return student

class StudentAuthenticationForm(forms.Form):
    pass
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

class TeacherRegistrationForm(UserCreationForm):
    pass
#     class Meta:
#         model = Teacher
#         fields = ['username', 'password1', 'password2']

class TeacherAuthenticationForm(forms.Form):
    pass
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
