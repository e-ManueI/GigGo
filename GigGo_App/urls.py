from django.urls import path, reverse_lazy
from GigGo_App.views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'GigGo_App'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('register/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name="signin.html", next_page=reverse_lazy('GigGo_App:dashboard')), name='login'),
    path('finder/', FinderHomeView.as_view(), name='finder_index'),
    path('search/', SearchView, name='search'),
    path('poster/createjob/', CreateJobView.as_view(), name='poster_createjob'),
    path('poster/deletejob/<int:pk>/', DeleteJobView.as_view(), name='poster_deletejob'),
    path('poster/updatejob/<int:pk>/', UpdateJobView.as_view(), name='poster_updatejob'),
    path('poster/joblist/', JobListView.as_view(), name='poster_joblist'),



]
