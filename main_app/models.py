from django.db import models
from django import forms
from django.contrib.auth.models import User 
from django.urls import reverse
from multiselectfield import MultiSelectField

INGREDIENT = (
    ("1", "Brandy"), ("2", "Gin"), ("3", "Rum"), ("4", "Tequila"),
    ("5", "Vodka"), ("6", "Whiskey"), ("7", "Vodka"), ("8", "Absinthe"),
    ("9", "Amaretto"), ("10", "Aperol"), ("11", "Baileys"), ("12", "Blue Curacao"),
    ("13", "Campari"), ("14", "Chambord"), ("15", "Chartreause Green"),
    ("16", "Chartreause Yellow"), ("17", "Cointreau"), ("18", "Creme de Cacao"),
    ("19", "Creme de Cassis"), ("20", "Creme de Menthe"), ("21", "Frangelico"),
    ("22", "Jagermeister"), ("23", "Kahlua"), ("24", "Midori"), ("25", "Triple Sec"),
    ("26", "Club Soda"), ("27", "Cola"), ("28", "Cranberry Juice"), ("29", "Cream"),
    ("30", "Diet Cola"), ("31", "Energy Drink"), ("32", "Ginger Ale"),
    ("33", "Ginger Beer"), ("34", "Grapefruit Juice"), ("35", "Lemon Juice"),
    ("36", "Lemon/Lime Soda"), ("37", "Lime Juice"), ("38", "Orange Juice"),
    ("39", "Simple Syrup"), ("40", "Tomato Juice"), ("41", "Tonic")
)

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    ingredients = MultiSelectField(choices = INGREDIENT, max_length=10)
    instructions = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, related_name='favorite', blank=True)
    
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
    