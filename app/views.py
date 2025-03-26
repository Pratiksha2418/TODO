from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    tasks=task.objects.all()
    return render(request,'index.html',{'tasks':tasks})
def toggle_completed(request,task_id):
    Task=task.objects.get(id=task_id)
    Task.completed=not Task.completed
    Task.save()
    return redirect('index')
def delete_task(request,task_id):
    Task=task.objects.get(id=task_id)
    Task.delete()
    return redirect('index')
