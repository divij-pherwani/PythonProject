from django import forms
from django.contrib.auth.models import User
from WebApp.models import StudentDetail, UniversityDetail, CourseDetail
from django.contrib.auth.forms import UserCreationForm


class LoginRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class StudentRegistrationForm(forms.ModelForm):
    student_name = forms.CharField(max_length=50)
    student_dob = forms.DateField(help_text="Format: YYYY-MM-DD")
    student_qualification = forms.CharField(max_length=15, help_text="None, High School, Undergraduate or Graduate")
    student_gender = forms.CharField(max_length=10, help_text="Male or Female")

    class Meta:
        model = StudentDetail
        fields = ("student_name", "student_dob", "student_qualification", "student_gender")


