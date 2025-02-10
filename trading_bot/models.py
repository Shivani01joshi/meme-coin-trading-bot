from django.db import models
from django.contrib.auth.models import User

class TradeOrder(models.Model):
    TRADE_TYPE_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Store who placed the order
    symbol = models.CharField(max_length=10)  # Example: BTCUSDT
    trade_type = models.CharField(max_length=4, choices=TRADE_TYPE_CHOICES)  # Buy/Sell
    quantity = models.FloatField()
    price = models.FloatField()  # Price at which trade was executed
    order_id = models.CharField(max_length=50, unique=True)  # Exchange order ID
    status = models.CharField(max_length=10, default="PENDING")  # Pending, Completed, Failed
    timestamp = models.DateTimeField(auto_now_add=True)  # Order placed time

    def __str__(self):
        return f"{self.user.username} - {self.trade_type} {self.quantity} {self.symbol} at {self.price}"
