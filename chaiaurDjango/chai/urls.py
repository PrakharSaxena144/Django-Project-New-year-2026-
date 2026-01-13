from django.urls import path
from . import views  # '.' refers to the current directory where urls.py is located



urlpatterns = [
    path('', views.all_chai, name='all_chai'),  # All Chai page
]