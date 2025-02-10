# trading_bot/management/commands/fetch_tokens.py
from django.core.management.base import BaseCommand
from trading_bot.utils import fetch_token_data  # or from .services import DexScreenerService

class Command(BaseCommand):
    help = 'Fetches token data from DEX Screener'

    def handle(self, *args, **kwargs):
        token_address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"  # Replace with actual token address
        data = fetch_token_data(token_address)  # or DexScreenerService.fetch_token_data(token_address)
        self.stdout.write(self.style.SUCCESS(f"Token Data: {data}"))