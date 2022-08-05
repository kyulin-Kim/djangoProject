from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
import json

def home(request):

    try:
        ticker = request.GET['ticker']
        stock_api = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_3420feef6d1c488bb72c294c39be92cc")
        stock = json.loads(stock_api.content)
    except Exception as e:
        stock = ""

    content = {'stock':stock}

    return render(request, 'stocks/home.html', content)