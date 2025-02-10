from binance.client import Client
from .models import TradeOrder
from django.contrib.auth.models import User
API_KEY = "Fy0iwDHP9B6mAeMbptCq3LWtaBo3R4K5UXumMTIWc85dSOlnQqL5YlWeQjCNitKu"
API_SECRET = "d5zOWGVAGMCxqaW2fbxOEhF70Ad610zFTIXK4G9OXeD1WkRotv4thuKdSkf7XTyi"

client = Client(API_KEY, API_SECRET,testnet=True)

#print(client)
#print(client.get_account())
#balances = client.get_account()["balances"]
#print(balances)
#print(client.get_account()["balances"])
def place_order(user_id, symbol, side, quantity):
    """
    Places a buy or sell order and stores it in the database.
    """
    try:
        user = User.objects.get(id=1)  # Ensure valid user
        #print(user)
        #print(symbol)
        
        # Debug Account Balance
        balance = client.get_asset_balance(asset="USDT")  # Replace with your asset
        print(f"💰 USDT Balance:", balance)
        #print("@")
        # Check if balance is enough
        if not balance or float(balance["free"]) < (quantity * 30000):  
            print("⚠️ Insufficient balance for trade!")
            return {"error": "Insufficient balance"}
        #print("1")
        # Place a MARKET order instead of LIMIT
        order = client.order_market_buy(symbol=symbol, quantity=quantity) if side.upper() == "BUY" else client.order_market_sell(symbol=symbol, quantity=quantity)

        # Print full response
        print("✅ Full Order Response:", order)
        #print(side)
        #print(quantity)
        # Extract order details
        order_id = order.get("orderId")
        #print(order_id)
        price = float(order["fills"][0]["price"]) if "fills" in order and order["fills"] else 0.0
        #print(price)
        status = order.get("status", "UNKNOWN")

        # Save order in the database
        trade_order = TradeOrder.objects.create(
            user=user,
            symbol=symbol,
            trade_type=side,
            quantity=quantity,
            price=price,
            order_id=order_id,
            status=status
        )
        
        return {"success": True, "order_id": order_id, "price": price}

    except User.DoesNotExist:
        return {"error": "User not found"}
    except Exception as e:
        return {"error": str(e)}
