# This the main controller file for the Django project.
# Views are used to handle requests and return responses in a Django application.

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to the Home Page of chaiaurDjango!, this is the home page...")
    return render(request, 'website/index.html')  # Render a template for the home page

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return HttpResponse("This is the Contact Page of chaiaurDjango!, get in touch with us.")
