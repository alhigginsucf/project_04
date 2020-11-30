from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import TickerForm
from .tiingo import get_meta_data, get_price_data, get_historical_data
import yfinance as yf
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
from django.conf import settings
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def getInfo( symbol):
    STARTDATE = '2014-01-01'
    ENDDATE = str( datetime.now().strftime('%Y-%m-%d'))
    company = yf.download( symbol, start=STARTDATE, end=ENDDATE)
    hist = company['Adj Close']
    hist.plot()
    plt.xlabel("Date")
    plt.ylabel("Adjusted")
    plt.title( symbol + " Price Data")
    #plt.show()
    IMGDIR = os.path.join( settings.BASE_DIR, 'stocks\static')
    plt.savefig( IMGDIR + '\my_plot.png')

def getStockInfo( request, symbol):
    getInfo( symbol)
    return JsonResponse({"symbol": symbol })

def index(request): 
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)
    else:
        form = TickerForm()
    return render(request, 'index.html', {'form': form})

def ticker(request, tid):
    context = {}
    context['ticker'] = tid
    context['meta'] = get_meta_data(tid)
    context['price'] = get_price_data(tid)
    context['history'] = get_historical_data(tid)
    return render(request, 'ticker.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'profile.html')