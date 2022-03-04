
from dataclasses import field
from api.models import Bitcoin, Ethereum, Solana, RandomTweetBTC, RandomTweetETH, RandomTweetSOL
from rest_framework import serializers


class BitcoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitcoin
        fields = ('id', 'price', 'price_change_percentage_24h', 'high_price_24h', 'market_dominance_percentage',
                  'keyword_tweet_number', 'datetime', 'semantics_all', 'semantics_positive_tweets', 'semantics_negative_tweets', 'circulating_supply',
                  'percentage_of_positive_tweets', 'percentage_of_negative_tweets', 'percentage_of_neutral_tweets', 'low_price_24h')


class EthereumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethereum
        fields = ('id', 'price', 'price_change_percentage_24h', 'high_price_24h', 'market_dominance_percentage',
                  'keyword_tweet_number', 'datetime', 'semantics_all', 'semantics_positive_tweets', 'semantics_negative_tweets', 'circulating_supply',
                  'percentage_of_positive_tweets', 'percentage_of_negative_tweets', 'percentage_of_neutral_tweets', 'low_price_24h')


class SolanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solana
        fields = ('id', 'price', 'price_change_percentage_24h', 'high_price_24h', 'market_dominance_percentage',
                  'keyword_tweet_number', 'datetime', 'semantics_all', 'semantics_positive_tweets', 'semantics_negative_tweets', 'circulating_supply',
                  'percentage_of_positive_tweets', 'percentage_of_negative_tweets', 'percentage_of_neutral_tweets', 'low_price_24h')


class RandomTweetBTCSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomTweetBTC
        fields = ('tweet', 'cleaned_tweet', 'eval')

class RandomTweetETHSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomTweetETH
        fields = ('tweet', 'cleaned_tweet', 'eval')
class RandomTweetSOLSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomTweetSOL
        fields = ('tweet', 'cleaned_tweet', 'eval')
