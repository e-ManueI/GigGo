from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(NewUser)
admin.site.register(Category)
admin.site.register(Job)
admin.site.register(JobApplication)
