from django.shortcuts import render, HttpResponse

def hello(request):
    return HttpResponse('<h1 style="color:red;"> Hello <h1>')
    

# Create your views here.
