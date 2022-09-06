from django.db import models
from django import forms
from django.contrib.auth.models import User 
from django.urls import reverse
from multiselectfield import MultiSelectField

INGREDIENT_CHOICES = (
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
    ingredients = forms.MultipleChoiceField(choices = INGREDIENT_CHOICES, widget=forms.CheckboxSelectMultiple())
    instructions = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'drink_id': self.id})

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     user_name = models.CharField(max_length=100)


### Original Code before undos ###
#     from django.db import models
# from django import forms
# from django.contrib.auth.models import User 
# from django.contrib.postgres.fields import ArrayField

# INGREDIENT_CHOICES = (
#     ("1", "Tequila"),
#     ("2", "Vodka"),
# )

# # Create your models here.
# class Drink(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.CharField(max_length=500)
#     ingredients = forms.MultipleChoiceField(choices = INGREDIENT_CHOICES)
#     instructions = models.TextField(max_length=1000)
    
#     def __str__(self):
#         return self.name

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     user_name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     #avatar = Image Link insert Here
#     favorites = ArrayField(
#         ArrayField(
#         drink = models.ForeignKey(Drink, on_delete=models.CASCADE),
#         size = 2
#     ),
#     size = 2,
# )
    