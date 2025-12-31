'''
Request handler for playground app

requests--> response
'''

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    # Pull data from database / process data / etc
    # Transform data / etc
    # Send email / etc
    return HttpResponse("Hello! Welcome to Django Playground App.")
