from django.shortcuts import render
from django.views.generic import TemplateView, View, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import UserSignUpForm
import logging


# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"
    
class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = UserSignUpForm
    success_url = reverse_lazy("GigGo_App:login")

    def form_invalid(self, form):
        logging.error(f'Invalid Form Data: {form.errors}')
        return super().form_invalid(form)
