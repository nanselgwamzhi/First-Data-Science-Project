from django.shortcuts import render
from django.http import HttpResponse
# create your views here

def index(request):
    return HttpResponse("You are highly welcome to Wokwok!")
