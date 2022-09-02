from django.shortcuts import render
from django.http import HttpResponse
from .models import Drink

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello World</h1>')

def index(request):
    drinks = Drink.objects.all()
    return render(request, 'index.html', {'drinks': drinks})

def userdrinks(request):
    return render(request, 'userdrinks.html')