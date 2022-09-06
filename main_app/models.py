from django.db import models
from django import forms
from django.contrib.auth.models import User 
from django.urls import reverse
from multiselectfield import MultiSelectField

INGREDIENT = (
    ("1", "Tequila"),
    ("2", "Vodka"),
    ("3", "Rum"),
    ("4", "Lemon"),
    ("5", "Coke"),
)

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    ingredients = MultiSelectField(choices = INGREDIENT, max_length=10)
    instructions = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'drink_id': self.id})

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()

