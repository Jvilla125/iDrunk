from django.db import models
from django import forms
from django.contrib.auth.models import User 

INGREDIENT_CHOICES = (
    ("1", "Tequila"),
    ("2", "Vodka"),
)

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    ingredients = forms.MultipleChoiceField(choices = INGREDIENT_CHOICES)
    instructions = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name