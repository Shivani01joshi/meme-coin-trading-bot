# trading_bot/urls.py
from django.urls import path
from .views import get_token_data

urlpatterns = [
    path('token/<str:token_address>/', get_token_data, name='get_token_data'),
]