from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Drink, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class DrinkCreate(LoginRequiredMixin, CreateView):
  model = Drink
  fields = ['name', 'image', 'ingredients', 'instructions']

  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class DrinkUpdate(LoginRequiredMixin, UpdateView): 
  model = Drink
  fields = ['name', 'image', 'ingredients', 'instructions']

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
    drinks = Drink.objects.all()
    return render(request, 'index.html', {'drinks': drinks})

@login_required
def userdrinks(request):
    drinks = Drink.objects.filter(user=request.user)
    return render(request, 'userdrinks.html', { 'drinks': drinks })

def logout_view(request):
    logout(request)
    success_url = '/index/'
    # Redirect to a success page.

def drinks_detail(request, drink_id):
  drink = Drink.objects.get(id=drink_id)
  return render(request, 'drinks/detail.html', {'drink': drink})

def fav_add(request, id):
  drink = get_object_or_404(Drink, id=id)
  if drink.favorites.filter(id=request.user.id).exists():
    drink.favorites.remove(request.user)
    print('!!!!!REMOVE FROM FAV!!!!!')
  else:
    drink.favorites.add(request.user)
    print('!!!!!ADD TO FAV!!!!!')
  return HttpResponseRedirect(request.META['HTTP_REFERER'])

def fav_drinks(request):
  favs = Drink.objects.filter(favorites=request.user.id)
  print(request.user.id, '<---------request.user: fav_drinks()')
  print(favs, '<---------favs: fav_drinks()')
  return render(request, 'drinks/favorites.html', {'favs':favs})

#class DrinkCreate(LoginRequiredMixin, CreateView):