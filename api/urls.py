from django.urls import path
from .views import GetBitcoin, GetEthereum, GetSolana

urlpatterns = [
    path('btc/', GetBitcoin.as_view()),
    path('eth/', GetEthereum.as_view()),
    path('sol/', GetSolana.as_view()),
]