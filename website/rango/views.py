from django.shortcuts import render
from django.http import HttpResponse


#----------------------------------------------------------------------
context_dict = {'boldmessage': "I am bold font from the context",
                    'name':"ardalan",                
                    
                    }
def index(request):
    
    return render (request,'index.html',context_dict)
def about(request):
    return render (request,'about.html',context_dict)
    
# Create your views here.
