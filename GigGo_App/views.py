from django.shortcuts import render
from django.views.generic import TemplateView, View, DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from .forms import UserSignUpForm, CreateJobForm
import logging
from .models import *


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


class JobListView(ListView):
    template_name = "joblist.html"
    model = Job


class CreateJobView(CreateView):
    template_name = "createjob.html"
    form_class = CreateJobForm


class DeleteJobView(DeleteView):
    template_name = "deletejob.html"
    model = Job
    success_url = reverse_lazy("GigGo_App:index")


class UpdateJobView(UpdateView):
    template_name = "updatejob.html"
    model = Job
    fields = "__all__"
    success_url = reverse_lazy("GigGo_App:index")
