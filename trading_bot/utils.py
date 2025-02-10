import requests
from django.core.cache import cache

def fetch_token_data(token_address):
    """Fetches token data from DexScreener API with caching."""
    cached_data = cache.get(token_address)
    if cached_data:
        return cached_data  # Return cached data if available

    url = f"https://api.dexscreener.com/latest/dex/tokens/{token_address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        cache.set(token_address, data, timeout=60)  # Cache data for 60 seconds
        return data
    else:
        return {"error": "Failed to fetch data from DexScreener"}
