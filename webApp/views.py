from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.text import capfirst


def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def project(request):
    return render(request,'project.html')

