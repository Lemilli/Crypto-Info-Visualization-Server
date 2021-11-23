from django.db import models

# Create your models here.

class Bitcoin(models.Model):
    price = models.FloatField()
    keyword_tweet_number = models.IntegerField
    tweet_content = models.CharField(max_length=300)
    datetime = models.DateTimeField()
    semantics = models.FloatField()

    def __str__(self):
        return self.tweet_content + "_" + self.price