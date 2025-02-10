# trading_bot/services.py
import requests

class DexScreenerService:
    @staticmethod
    def fetch_token_data(token_address):
        url = f"https://api.dexscreener.com/latest/dex/tokens/{token_address}"
        response = requests.get(url)
        return response.json()