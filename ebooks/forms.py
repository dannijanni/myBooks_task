from django import forms
from .models import myBooks

class MyBooksForm(forms.ModelForm):
    class Meta:
        model = myBooks
        fields = ['title', 'author', 'genre', 'price', 'stock']
