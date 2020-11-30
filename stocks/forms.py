from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TickerForm(forms.Form):
    ticker = forms.CharField(label='Ticker', max_length=5)

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']