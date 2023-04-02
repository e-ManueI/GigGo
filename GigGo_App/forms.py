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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'location': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter job description', 'placeholder': 'Enter Job Category'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'status': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Status'}),
        }
