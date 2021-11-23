# Create your tasks here

from datetime import datetime
from .models import Bitcoin

from celery import shared_task


@shared_task
def create_new_object():
    print("Task started!!!")
    new_object = Bitcoin.objects.create(price=1, keyword_tweet_number=1, tweet_content='tweet',
                                        datetime=datetime.now(), semantics=0.5)
    return new_object.tweet_content
