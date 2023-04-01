from django.urls import path, reverse_lazy
from GigGo_App.views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'GigGo_App'


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('register/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name="signin.html",
         next_page=reverse_lazy('GigGo_App:dashboard')), name='login'),
    path('createjob/', CreateJobView.as_view(), name='createjob'),
    path('deletejob/<int:pk>/', DeleteJobView.as_view(), name='deletejob'),
    path('updatejob/<int:pk>/', UpdateJobView.as_view(), name='updatejob'),
    path('joblist/', JobListView.as_view(), name='joblist'),



]
