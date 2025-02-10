# trading_bot/management/commands/fetch_tokens.py
from django.core.management.base import BaseCommand
from trading_bot.utils import fetch_token_data  

from trading_bot.trading import place_order  # Import order function
from django.contrib.auth import get_user_model
from django.utils.timezone import now

class Command(BaseCommand):
    help = 'Fetches token data from DEX Screener and executes trades'

    def handle(self, *args, **kwargs):
        token_address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"  # Example USDT token
        data = fetch_token_data(token_address)  

        if "pairs" in data and len(data["pairs"]) > 0:
            latest_price = float(data["pairs"][0]["priceUsd"])  # Extract token price

            # Define trade conditions
            BUY_THRESHOLD = 1.0  # Example: Buy when price is <= $1.0
            SELL_THRESHOLD = 1.5  # Example: Sell when price is >= $1.5

            # Get a user (modify this to select a real user)
            User = get_user_model()
            user = User.objects.first()  # Get first user (Modify for actual logic)
            #print(user)
            if user:
                if latest_price <= BUY_THRESHOLD:
                    self.stdout.write(self.style.SUCCESS(f"Buying at ${latest_price}"))
                    place_order(user, "BTCUSDT", "BUY", 0.001)  # Example order

                elif latest_price >= SELL_THRESHOLD:
                    self.stdout.write(self.style.SUCCESS(f"Selling at ${latest_price}"))
                    place_order(user, "BTCUSDT", "SELL", 0.001)  # Example order

            self.stdout.write(self.style.SUCCESS(f"Token Price: ${latest_price}"))

        else:
            self.stdout.write(self.style.ERROR("Failed to retrieve token data."))
