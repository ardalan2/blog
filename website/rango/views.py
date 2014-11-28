from django.shortcuts import render
from django.http import HttpResponse

#----------------------------------------------------------------------
def index(request):
    return HttpResponse("Rango says hey world! <a href='/rango/about'>About</a>")
def about(request):
    return HttpResponse("This is the about page!<a href='/rango'>Index</a>")
    
# Create your views here.
