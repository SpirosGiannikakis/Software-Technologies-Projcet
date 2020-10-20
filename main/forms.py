from django import forms
from django.forms import ModelForm
from .models import *

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name','address','phone','description','averageRating','image')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")