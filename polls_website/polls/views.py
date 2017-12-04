from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Polls App - Welcome")

# Create your views here.
