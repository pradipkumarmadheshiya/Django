from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class ReviewForm(forms.Form):
    username=forms.CharField(max_length=50)