from django.urls import path
from .views import GetBitcoin, GetEthereum, GetSolana, GetRandomTweetBTC, GetRandomTweetETH, GetRandomTweetSOL

urlpatterns = [
    path('btc/', GetBitcoin.as_view()),
    path('eth/', GetEthereum.as_view()),
    path('sol/', GetSolana.as_view()),
    path('random_tweet_btc/', GetRandomTweetBTC.as_view()),
    path('random_tweet_eth/', GetRandomTweetETH.as_view()),
    path('random_tweet_sol/', GetRandomTweetSOL.as_view()),
]