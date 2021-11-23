
from api.models import Bitcoin
from rest_framework import serializers


class BitcoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitcoin
        fields = ('id', 'price', 'keyword_tweet_number', 'tweet_content', 'datetime', 'semantics')
