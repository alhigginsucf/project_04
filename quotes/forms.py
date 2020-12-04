from django import forms
from .models import Stock, Trade, Position
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["ticker"]
    
class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ["stock_name", "quantity", "price", "trade_type"]

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ["stock_name", "quantity", "average"]

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class TickerForm(forms.Form):
    ticker = forms.CharField(label='Enter Ticker', max_length=5)