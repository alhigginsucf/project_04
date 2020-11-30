import requests
import yfinance as yf
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
from django.conf import settings
import os


headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 8522ae8156705d93eab82e7b1a551d898512db27',
}

def get_meta_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()

def get_price_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}/prices".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()[0]

def get_historical_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}/prices?startDate=2012-1-1&endDate=2016-1-1.".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()[0]
