from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse
from multiselectfield import MultiSelectField

INGREDIENT = (
    ("1", "Brandy"), ("2", "Gin"), ("3", "Rum"), ("4", "Tequila"),
    ("5", "Vodka"), ("6", "Whiskey"), ("7", "Whiskey Scotch"), ("8", "Absinthe"),
    ("9", "Amaretto"), ("10", "Aperol"), ("11", "Baileys"), ("12", "Blue Curacao"),
    ("13", "Campari"), ("14", "Chambord"), ("15", "Chartreause Green"),
    ("16", "Chartreause Yellow"), ("17", "Cointreau"), ("18", "Creme de Cacao"),
    ("19", "Creme de Cassis"), ("20", "Creme de Menthe"), ("21", "Frangelico"),
    ("22", "Jagermeister"), ("23", "Kahlua"), ("24", "Midori"), ("25", "Triple Sec"),
    ("43", "Vermouth Dry"), ("44", "Vermouth Sweet"),
    ("26", "Club Soda"), ("27", "Cola"), ("28", "Cranberry Juice"), ("29", "Cream"),
    ("30", "Diet Cola"), ("31", "Energy Drink"), ("32", "Ginger Ale"),
    ("33", "Ginger Beer"), ("34", "Grapefruit Juice"), ("35", "Lemon Juice"),
    ("36", "Lemon/Lime Soda"), ("37", "Lime Juice"), ("38", "Orange Juice"),
    ("39", "Simple Syrup"), ("40", "Sour Mix"), ("41", "Tomato Juice"), ("42", "Tonic")
)

# Create your models here.


class Drink(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    ingredients = MultiSelectField(choices=INGREDIENT, max_length=50)
    instructions = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(
        User, related_name='favorite', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'drink_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for drink_id: {self.drink_id} @{self.url}"


class Review(models.Model):
    RATING_CHOICES = (
        ('1', '🍹'),
        ('2', '🍹🍹'),
        ('3', '🍹🍹🍹'),
        ('4', '🍹🍹🍹🍹'),
        ('5', '🍹🍹🍹🍹🍹'),
    )

    date = models.DateField(auto_now_add=True)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, blank=True)
    review = models.TextField(max_length=300, blank=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.drink} - {self.rating}'
