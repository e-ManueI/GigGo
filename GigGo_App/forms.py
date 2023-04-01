from django import forms
from django.contrib.auth.forms import UserCreationForm
from GigGo_App.models import NewUser, Job

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Retype-Password'}),

        }

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
