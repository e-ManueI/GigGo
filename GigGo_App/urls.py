from django.urls import path, reverse_lazy
from GigGo_App.views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'GigGo_App'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('register/', SignUpView.as_view(), name='signup'),
    path('poster/dashboard/', UserDashboardView.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(template_name="signin.html", next_page=reverse_lazy('GigGo_App:dashboard')), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('GigGo_App:login')), name='logout'),
    path('finder/', FinderHomeView.as_view(), name='finder_index'),
    path('search/', SearchView, name='search'),
    path('poster/createjob/', CreateJobView.as_view(), name='poster_createjob'),
    path('poster/joblist/', JobListView.as_view(), name='poster_joblist'),
    path('poster/updatejob/<int:pk>/', UpdateJobView.as_view(), name='poster_updatejob'),
    path('poster/deletejob/<int:pk>/', DeleteJobView.as_view(), name='poster_deletejob'),

]
