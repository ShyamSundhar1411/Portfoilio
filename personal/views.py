from django.shortcuts import render
from .models import Project


def home(request):
    a = Project.objects.all()
    return render(request,'personal/home.html',{'data':a})
