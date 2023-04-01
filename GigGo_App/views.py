from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import TemplateView, View, DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from .forms import UserSignUpForm, CreateJobForm
import logging
from django.contrib import messages
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#################################################################################
# Login Mixins
#################################################################################
class FinderRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    raise_exception = True
    permission_denied_message = "Job finder access only"
    login_url = 'GigGo_App:login'

    def test_func(self):
        return self.request.user.is_finder


class PosterRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    raise_exception = True
    permission_denied_message = "Job owner access only"
    login_url = 'GigGo_App:login'

    def test_func(self):
        return self.request.user.is_poster


#################################################################################
# General Views
#################################################################################
class HomePageView(TemplateView):
    template_name = "index.html"


class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = UserSignUpForm
    success_url = reverse_lazy("GigGo_App:login")

    def form_invalid(self, form):
        logging.error(f'Invalid Form Data: {form.errors}')
        return super().form_invalid(form)
    

#################################################################################
# Job Poster Views
#################################################################################
class JobListView(PosterRequiredMixin, ListView):
    template_name = "poster_joblist.html"
    model = Job


class CreateJobView(PosterRequiredMixin, CreateView):
    template_name = "poster_createjob.html"
    form_class = CreateJobForm


class DeleteJobView(PosterRequiredMixin, DeleteView):
    template_name = "poster_deletejob.html"
    model = Job
    success_url = reverse_lazy("GigGo_App:index")


class UpdateJobView(PosterRequiredMixin, UpdateView):
    template_name = "poster_updatejob.html"
    model = Job
    fields = "__all__"
    success_url = reverse_lazy("GigGo_App:index")


#################################################################################
# Job Finder Views
#################################################################################
class FinderHomeView(TemplateView):
    def get(self, request):
        # print(Category.objects.all())
        data = {
            "categories": Category.objects.all(),
            "locations": Job.LOCATION
        }
        return render(request, 'finder.html', data)

def SearchView(request):
    # query = request.GET.get('q')
    results = Job.objects.all()
    category = request.GET.get('category')
    location = request.GET.get('location')
    if not category and not location:
        messages.warning(request, 'Please select a Category or Location')
        return render(request, 'feed/index.html', {"categories": Category.objects.all(),
                                                   "locations": Job.LOCATION
                                                   })
    # words = query.split()
    # results = Job.objects.filter(
        # reduce(lambda x, y: x | y, [Q(name__icontains=word) for word in words])).order_by('-name')
    results = results.filter(category__name__iexact=category)
    # print(category)
    results = results.filter(location__iexact=location)
    # print(location)
    if not results:
        messages.warning(
            request, 'No results found for query: {}, {}'.format(category.upper(), location.upper()))
        return redirect('GigGo_App:index')
    paginator = Paginator(results, 10)  # Show 10 results per page
    page = request.GET.get('page')
    results = paginator.get_page(page)
    context = {
        "results": results,
        "categories": Category.objects.all(),
        "locations": Job.LOCATION
    }
    return render(request, 'jobs.html', context)
