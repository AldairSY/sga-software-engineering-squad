from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def login_view(request):
    return HttpResponse("Login base SGA")