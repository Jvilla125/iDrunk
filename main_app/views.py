from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Drink, User, Photo, Review
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReviewForm
from django.db.models import Avg

import uuid
import boto3 

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'idrunk-collection'

class DrinkCreate(LoginRequiredMixin, CreateView):
  model = Drink
  fields = ['name', 'ingredients', 'instructions']

  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class DrinkUpdate(LoginRequiredMixin, UpdateView): 
  model = Drink
  fields = ['name', 'ingredients', 'instructions']

  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class DrinkDelete(LoginRequiredMixin,DeleteView):
  model = Drink
  success_url = '/index/'

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
    return render(request, 'home.html')

def index(request):
    drinks = Drink.objects.order_by('name')
    return render(request, 'index.html', {'drinks': drinks})

@login_required
def userdrinks(request):
    drinks = Drink.objects.filter(user=request.user).order_by('name')
    return render(request, 'userdrinks.html', { 'drinks': drinks })

def logout_view(request):
    logout(request)
    success_url = '/index/'

def drinks_detail(request, drink_id):
  drink = Drink.objects.get(id=drink_id)
  favs = Drink.objects.filter(favorites=request.user.id)
  drinks_rev = Review.objects.filter(drink=drink_id)
  sum = 0
  for r in drinks_rev:
    sum += int(r.rating)
  if sum == 0:
    average = 0
  else: 
    average = round(sum / len(drinks_rev), 1)
  form = ReviewForm(request.POST)
  return render(request, 'drinks/detail.html', {'drink': drink, 'favs': favs, 'review_form': form, 'average': average})

def fav_add(request, id):
  drink = get_object_or_404(Drink, id=id)
  if drink.favorites.filter(id=request.user.id).exists():
    drink.favorites.remove(request.user)
  else:
    drink.favorites.add(request.user)
  return HttpResponseRedirect(request.META['HTTP_REFERER'])

def fav_drinks(request):
  favs = Drink.objects.filter(favorites=request.user.id).order_by('name')
  return render(request, 'drinks/favorites.html', {'favs':favs})

@login_required
def add_photo(request, drink_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, drink_id=drink_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', drink_id=drink_id)
  
@login_required
def add_review(request, drink_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
      new_review = form.save(commit=False)
      new_review.drink_id = drink_id
      new_review.user = request.user
      new_review.save()
  return redirect('detail', drink_id=drink_id)

