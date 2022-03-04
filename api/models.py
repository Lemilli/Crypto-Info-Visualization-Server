from django.db import models

# Create your models here.

class Bitcoin(models.Model):
    price = models.FloatField()
    price_change_percentage_24h = models.FloatField()
    high_price_24h = models.FloatField()
    low_price_24h = models.FloatField()
    market_dominance_percentage = models.FloatField()
    circulating_supply = models.FloatField()

    keyword_tweet_number = models.IntegerField()
    datetime = models.DateTimeField()
    semantics_all = models.FloatField()
    semantics_positive_tweets = models.FloatField()
    semantics_negative_tweets = models.FloatField()

    percentage_of_positive_tweets = models.FloatField()
    percentage_of_negative_tweets = models.FloatField()
    percentage_of_neutral_tweets = models.FloatField()

    def __str__(self):
        return 'Bitcoin ' + str(self.datetime)

class Ethereum(models.Model):
    price = models.FloatField()
    price_change_percentage_24h = models.FloatField()
    high_price_24h = models.FloatField()
    low_price_24h = models.FloatField()
    market_dominance_percentage = models.FloatField()
    circulating_supply = models.FloatField()

    keyword_tweet_number = models.IntegerField()
    datetime = models.DateTimeField()
    semantics_all = models.FloatField()
    semantics_positive_tweets = models.FloatField()
    semantics_negative_tweets = models.FloatField()

    percentage_of_positive_tweets = models.FloatField()
    percentage_of_negative_tweets = models.FloatField()
    percentage_of_neutral_tweets = models.FloatField()

    def __str__(self):
        return 'Ethereum ' + str(self.datetime)

class Solana(models.Model):
    price = models.FloatField()
    price_change_percentage_24h = models.FloatField()
    high_price_24h = models.FloatField()
    low_price_24h = models.FloatField()
    market_dominance_percentage = models.FloatField()
    circulating_supply = models.FloatField()

    keyword_tweet_number = models.IntegerField()
    datetime = models.DateTimeField()
    semantics_all = models.FloatField()
    semantics_positive_tweets = models.FloatField()
    semantics_negative_tweets = models.FloatField()

    percentage_of_positive_tweets = models.FloatField()
    percentage_of_negative_tweets = models.FloatField()
    percentage_of_neutral_tweets = models.FloatField()

    def __str__(self):
        return 'Solana ' + str(self.datetime)

class RandomTweetBTC(models.Model):
    tweet = models.CharField(max_length=300)
    cleaned_tweet = models.CharField(max_length=300)
    eval = models.FloatField()

    def __str__(self):
        return 'Bitcoin ' + str(self.eval)

class RandomTweetETH(models.Model):
    tweet = models.CharField(max_length=300)
    cleaned_tweet = models.CharField(max_length=300)
    eval = models.FloatField()

    def __str__(self):
        return 'Ethereum ' + str(self.eval)

class RandomTweetSOL(models.Model):
    tweet = models.CharField(max_length=300)
    cleaned_tweet = models.CharField(max_length=300)
    eval = models.FloatField()

    def __str__(self):
        return 'Solana' + str(self.eval)

