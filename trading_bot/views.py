from django.shortcuts import render
from django.http import JsonResponse
import requests
from .utils import fetch_token_data  

def fetch_token_data(request, token_address):
    token_address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"  # USDT on Ethereum
    url = f"https://api.dexscreener.com/latest/dex/tokens/{token_address}"
    
    response = requests.get(url)
    print(response)
    return JsonResponse(response.json())

def get_token_data(request, token_address):
    data = fetch_token_data(token_address) 
    return JsonResponse(data)