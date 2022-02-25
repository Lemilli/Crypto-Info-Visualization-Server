# Create your tasks here

from datetime import datetime, timedelta
from .models import Bitcoin, Ethereum, Solana
import requests

from celery import shared_task
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import statistics
from random import randint
import re
from html import unescape

# Codes for all 3 tasks are identical
@shared_task
def add_bitcoin_to_db():
    # ------------------------------------------------------------------------------------------
    # This part gets tweet count containing keyword "bitcoin" for each minute
    # ------------------------------------------------------------------------------------------

    # get time in UTC, minus 20 seconds is twitter API limit
    d = datetime.utcnow() - timedelta(seconds=20)
    start_time_unformatted = d - timedelta(minutes=1)

    # formatting as twitter API requests
    start_time = start_time_unformatted.isoformat("T") + "Z"
    end_time = d.isoformat("T") + "Z"

    count_response = requests.get('https://api.twitter.com/2/tweets/counts/recent', params={
        'query': 'bitcoin',
        'start_time': start_time,
        'end_time': end_time,
    }, headers={
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAFBHUgEAAAAAS%2FqmgRmQ9Et4NnVHwquTNcgLSh4%3DlVJtc0IVsXGsJ37OybtqRC61spliYMfhyKKZtRCqnHa8tZUsQc'
    }).json()

    tweet_count = count_response['meta']['total_tweet_count']

    # ------------------------------------------------------------------------------------------
    # Done with tweet_count, moving on to tweet_contents and its analysis to calculate semantics
    # ------------------------------------------------------------------------------------------

    tweet_contents_response = requests.get('https://api.twitter.com/2/tweets/search/recent', params={
        # ensures there wull be no retweets and replies
        'query': '(BITCOIN OR BTC) -is:retweet -is:reply lang:en',
        'start_time': start_time,
        'end_time': end_time,
        'max_results': 80,
    }, headers={
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAFBHUgEAAAAAS%2FqmgRmQ9Et4NnVHwquTNcgLSh4%3DlVJtc0IVsXGsJ37OybtqRC61spliYMfhyKKZtRCqnHa8tZUsQc'
    }).json()

    tweet_contents_list = tweet_contents_response['data']
    total_length = tweet_contents_response['meta']['result_count']

    analyzer = SentimentIntensityAnalyzer()
    compound_scores = []

    # Clean and analyze each tweet and add its semantics value to the array so we can get the average later
    for tweet in tweet_contents_list:
        text = tweet['text']
        cleaned_tweet = clean_tweet(text)
        vs = analyzer.polarity_scores(cleaned_tweet)
        compound_scores.append(vs['compound'])

    # # Choose and evaluate random tweet
    # rand_index = randint(0, total_length-1)
    # rand_tweet = tweet_contents_list[rand_index]['text']
    # rand_compound_score = compound_scores[rand_index]

    # print(rand_tweet)
    # print(rand_compound_score)

    positive_tweets = []
    negative_tweets = []
    neutral_tweets_count = 0
    for value in compound_scores:
        if value >= 0.05:
            positive_tweets.append(value)
        elif value <= -0.05:
            negative_tweets.append(value)
        else:
            neutral_tweets_count += 1

    # formula is sum / length of the array
    average_compound = statistics.mean(
        compound_scores) if len(compound_scores) != 0 else 0
    average_positive_tweets = statistics.mean(
        positive_tweets) if len(positive_tweets) != 0 else 0
    average_negative_tweets = statistics.mean(
        negative_tweets) if len(negative_tweets) != 0 else 0

    # Count percentages
    positive_tweets_percentage = len(positive_tweets) / total_length
    negative_tweets_percentage = len(negative_tweets) / total_length
    neutral_tweets_percentage = neutral_tweets_count / total_length

    # ------------------------------------------------------------------------------------------
    # Done with semantics, moving on to getting bitcoin price
    # ------------------------------------------------------------------------------------------

    bitcoin_price_response = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin', params={
        'tickers': 'false',
        'community_data': 'false',
        'developer_data': 'false',
        'sparkline': 'false',
    }, headers={
        'accept': 'application/json'
    }).json()

    current_price = bitcoin_price_response['market_data']['current_price']['usd']
    price_change_percentage_24h = bitcoin_price_response['market_data']['price_change_percentage_24h']
    high_price_24h = bitcoin_price_response['market_data']['high_24h']['usd']
    low_price_24h = bitcoin_price_response['market_data']['low_24h']['usd']
    circulating_supply = bitcoin_price_response['market_data']['circulating_supply']

    crypto_global_response = requests.get('https://api.coingecko.com/api/v3/global', headers={
        'accept': 'application/json'
    }).json()

    market_dominance_percentage = crypto_global_response['data']['market_cap_percentage']['btc']

    Bitcoin.objects.create(price=current_price,
                           price_change_percentage_24h=price_change_percentage_24h,
                           high_price_24h=high_price_24h,
                           market_dominance_percentage=market_dominance_percentage,
                           keyword_tweet_number=tweet_count,
                           datetime=end_time,
                           semantics_all=average_compound,
                           semantics_positive_tweets=average_positive_tweets,
                           semantics_negative_tweets=average_negative_tweets,
                           circulating_supply=circulating_supply,
                           percentage_of_positive_tweets=positive_tweets_percentage,
                           percentage_of_negative_tweets=negative_tweets_percentage,
                           percentage_of_neutral_tweets=neutral_tweets_percentage,
                           low_price_24h=low_price_24h)

    return 'Bitcoin: ' + str(current_price)


@shared_task
def add_ethereum_to_db():
    # ------------------------------------------------------------------------------------------
    # This part gets tweet count containing keyword "Ethereum" for each minute
    # ------------------------------------------------------------------------------------------

    # get time in UTC, minus 20 seconds is twitter API limit
    d = datetime.utcnow() - timedelta(seconds=20)
    start_time_unformatted = d - timedelta(minutes=1)

    # formatting as twitter API requests
    start_time = start_time_unformatted.isoformat("T") + "Z"
    end_time = d.isoformat("T") + "Z"

    count_response = requests.get('https://api.twitter.com/2/tweets/counts/recent', params={
        'query': 'ethereum',
        'start_time': start_time,
        'end_time': end_time,
    }, headers={
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAFBHUgEAAAAAS%2FqmgRmQ9Et4NnVHwquTNcgLSh4%3DlVJtc0IVsXGsJ37OybtqRC61spliYMfhyKKZtRCqnHa8tZUsQc'
    }).json()

    tweet_count = count_response['meta']['total_tweet_count']

    # ------------------------------------------------------------------------------------------
    # Done with tweet_count, moving on to tweet_contents and its analysis to calculate semantics
    # ------------------------------------------------------------------------------------------

    tweet_contents_response = requests.get('https://api.twitter.com/2/tweets/search/recent', params={
        # ensures there wull be no retweets and replies
        'query': '(ETHEREUM OR ETH) -is:retweet -is:reply lang:en',
        'start_time': start_time,
        'end_time': end_time,
        'max_results': 80,
    }, headers={
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAFBHUgEAAAAAS%2FqmgRmQ9Et4NnVHwquTNcgLSh4%3DlVJtc0IVsXGsJ37OybtqRC61spliYMfhyKKZtRCqnHa8tZUsQc'
    }).json()

    tweet_contents_list = tweet_contents_response['data']
    total_length = tweet_contents_response['meta']['result_count']

    analyzer = SentimentIntensityAnalyzer()
    compound_scores = []

    # Clean and analyze each tweet and add its semantics value to the array so we can get the average later
    for tweet in tweet_contents_list:
        text = tweet['text']
        cleaned_tweet = clean_tweet(text)
        vs = analyzer.polarity_scores(cleaned_tweet)
        compound_scores.append(vs['compound'])

    positive_tweets = []
    negative_tweets = []
    neutral_tweets_count = 0
    for value in compound_scores:
        if value >= 0.05:
            positive_tweets.append(value)
        elif value <= -0.05:
            negative_tweets.append(value)
        else:
            neutral_tweets_count += 1

    # formula is sum / length of the array
    average_compound = statistics.mean(
        compound_scores) if len(compound_scores) != 0 else 0
    average_positive_tweets = statistics.mean(
        positive_tweets) if len(positive_tweets) != 0 else 0
    average_negative_tweets = statistics.mean(
        negative_tweets) if len(negative_tweets) != 0 else 0

    # Count percentages
    positive_tweets_percentage = len(positive_tweets) / total_length
    negative_tweets_percentage = len(negative_tweets) / total_length
    neutral_tweets_percentage = neutral_tweets_count / total_length

    # ------------------------------------------------------------------------------------------
    # Done with semantics, moving on to getting price
    # ------------------------------------------------------------------------------------------

    price_response = requests.get('https://api.coingecko.com/api/v3/coins/ethereum', params={
        'tickers': 'false',
        'community_data': 'false',
        'developer_data': 'false',
        'sparkline': 'false',
    }, headers={
        'accept': 'application/json'
    }).json()

    current_price = price_response['market_data']['current_price']['usd']
    price_change_percentage_24h = price_response['market_data']['price_change_percentage_24h']
    high_price_24h = price_response['market_data']['high_24h']['usd']
    low_price_24h = price_response['market_data']['low_24h']['usd']
    circulating_supply = price_response['market_data']['circulating_supply']

    crypto_global_response = requests.get('https://api.coingecko.com/api/v3/global', headers={
        'accept': 'application/json'
    }).json()

    market_dominance_percentage = crypto_global_response['data']['market_cap_percentage']['eth']

    Ethereum.objects.create(price=current_price,
                            price_change_percentage_24h=price_change_percentage_24h,
                            high_price_24h=high_price_24h,
                            market_dominance_percentage=market_dominance_percentage,
                            keyword_tweet_number=tweet_count,
                            datetime=end_time,
                            semantics_all=average_compound,
                            semantics_positive_tweets=average_positive_tweets,
                            semantics_negative_tweets=average_negative_tweets,
                            circulating_supply=circulating_supply,
                            percentage_of_positive_tweets=positive_tweets_percentage,
                            percentage_of_negative_tweets=negative_tweets_percentage,
                            percentage_of_neutral_tweets=neutral_tweets_percentage,
                            low_price_24h=low_price_24h)

    return 'Ethereum: ' + str(current_price)


@shared_task
def add_solana_to_db():
    # ------------------------------------------------------------------------------------------
    # This part gets tweet count containing keyword "Solana" for each minute
    # ------------------------------------------------------------------------------------------

    # get time in UTC, minus 20 seconds is twitter API limit
    d = datetime.utcnow() - timedelta(seconds=20)
    start_time_unformatted = d - timedelta(minutes=1)

    # formatting as twitter API requests
    start_time = start_time_unformatted.isoformat("T") + "Z"
    end_time = d.isoformat("T") + "Z"

    count_response = requests.get('https://api.twitter.com/2/tweets/counts/recent', params={
        'query': 'solana',
        'start_time': start_time,
        'end_time': end_time,
    }, headers={
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAFBHUgEAAAAAS%2FqmgRmQ9Et4NnVHwquTNcgLSh4%3DlVJtc0IVsXGsJ37OybtqRC61spliYMfhyKKZtRCqnHa8tZUsQc'
    }).json()

    tweet_count = count_response['meta']['total_tweet_count']

    # ------------------------------------------------------------------------------------------
    # Done with tweet_count, moving on to tweet_contents and its analysis to calculate semantics
    # ------------------------------------------------------------------------------------------

    tweet_contents_response = requests.get('https://api.twitter.com/2/tweets/search/recent', params={
        # ensures there wull be no retweets and replies
        'query': '(SOLANA OR SOL) -is:retweet -is:reply lang:en',
        'start_time': start_time,
        'end_time': end_time,
        'max_results': 80,
    }, headers={
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAFBHUgEAAAAAS%2FqmgRmQ9Et4NnVHwquTNcgLSh4%3DlVJtc0IVsXGsJ37OybtqRC61spliYMfhyKKZtRCqnHa8tZUsQc'
    }).json()

    tweet_contents_list = tweet_contents_response['data']
    total_length = tweet_contents_response['meta']['result_count']

    analyzer = SentimentIntensityAnalyzer()
    compound_scores = []

    # Clean and analyze each tweet and add its semantics value to the array so we can get the average later
    for tweet in tweet_contents_list:
        text = tweet['text']
        cleaned_tweet = clean_tweet(text)
        vs = analyzer.polarity_scores(cleaned_tweet)
        compound_scores.append(vs['compound'])

    positive_tweets = []
    negative_tweets = []
    neutral_tweets_count = 0
    for value in compound_scores:
        if value >= 0.05:
            positive_tweets.append(value)
        elif value <= -0.05:
            negative_tweets.append(value)
        else:
            neutral_tweets_count += 1

    # formula is sum / length of the array
    average_compound = statistics.mean(
        compound_scores) if len(compound_scores) != 0 else 0
    average_positive_tweets = statistics.mean(
        positive_tweets) if len(positive_tweets) != 0 else 0
    average_negative_tweets = statistics.mean(
        negative_tweets) if len(negative_tweets) != 0 else 0

    # Count percentages
    positive_tweets_percentage = len(positive_tweets) / total_length
    negative_tweets_percentage = len(negative_tweets) / total_length
    neutral_tweets_percentage = neutral_tweets_count / total_length

    # ------------------------------------------------------------------------------------------
    # Done with semantics, moving on to getting price
    # ------------------------------------------------------------------------------------------

    price_response = requests.get('https://api.coingecko.com/api/v3/coins/solana', params={
        'tickers': 'false',
        'community_data': 'false',
        'developer_data': 'false',
        'sparkline': 'false',
    }, headers={
        'accept': 'application/json'
    }).json()

    current_price = price_response['market_data']['current_price']['usd']
    price_change_percentage_24h = price_response['market_data']['price_change_percentage_24h']
    high_price_24h = price_response['market_data']['high_24h']['usd']
    low_price_24h = price_response['market_data']['low_24h']['usd']
    circulating_supply = price_response['market_data']['circulating_supply']

    crypto_global_response = requests.get('https://api.coingecko.com/api/v3/global', headers={
        'accept': 'application/json'
    }).json()

    market_dominance_percentage = crypto_global_response['data']['market_cap_percentage']['sol']


    Solana.objects.create(price=current_price,
                          price_change_percentage_24h=price_change_percentage_24h,
                          high_price_24h=high_price_24h,
                          market_dominance_percentage=market_dominance_percentage,
                          keyword_tweet_number=tweet_count,
                          datetime=end_time,
                          semantics_all=average_compound,
                          semantics_positive_tweets=average_positive_tweets,
                          semantics_negative_tweets=average_negative_tweets,
                          circulating_supply=circulating_supply,
                          percentage_of_positive_tweets=positive_tweets_percentage,
                          percentage_of_negative_tweets=negative_tweets_percentage,
                          percentage_of_neutral_tweets=neutral_tweets_percentage,
                          low_price_24h=low_price_24h)

    return 'Solana: ' + str(current_price)


def clean_tweet(text):
    # convert html characters into UTF-8 format
    # e.g., convert &amp into &
    cleaned_tweet = unescape(text)

    # In order: remove mentions, hashtags, links, multiple spaces in a row
    cleaned_tweet = re.sub("@[A-Za-z0-9_]+","", text)
    cleaned_tweet = re.sub("#[A-Za-z0-9_]+","", cleaned_tweet)
    cleaned_tweet = re.sub(r'https?://\S+|www\.\S+', " ", cleaned_tweet)
    cleaned_tweet = re.sub(' +', ' ', cleaned_tweet)

    return cleaned_tweet