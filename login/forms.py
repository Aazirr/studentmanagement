from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Instructor

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class InstructorForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Instructor
        fields = ['username', 'password', 'instructor_id', 'first_name', 'last_name', 'email', 'phone_number']