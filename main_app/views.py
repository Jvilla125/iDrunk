from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Drink

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
    return HttpResponse('<h1>Hello World</h1>')

def index(request):
    drinks = Drink.objects.all()
    return render(request, 'index.html', {'drinks': drinks})

def userdrinks(request):
    return render(request, 'userdrinks.html')

def logout_view(request):
    logout(request)
    success_url = '/index/'
    # Redirect to a success page.