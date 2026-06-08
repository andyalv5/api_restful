from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

#ESTO NO ES NECESARIO PARA EL TASK
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{'form': UserCreationForm})
    else:
        if request.POST['password1']== request.POST['password2']:
            #register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                redirect()
            except:
                return render(request, 'signup.html',{'form': UserCreationForm, 'error': 'User already exists'})

        else:
            return render(request, 'signup.html',{'form': UserCreationForm, 'error': 'Password do not Match'})

def task(request):
    return render(request, 'task.html')
