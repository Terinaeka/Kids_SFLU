from django.http import HttpResponse
from  django.shortcuts import render
from .models import Todo

def index(request):
    todos=Todo.objects.all()
    return render (request, 'main/index.html', {'todos':todos})

def contact(request):
    return HttpResponse("<h1>Наші</h1>")