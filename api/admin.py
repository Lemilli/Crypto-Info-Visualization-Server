from django.contrib import admin
from .models import Bitcoin, Ethereum, Solana, RandomTweetBTC, RandomTweetETH, RandomTweetSOL


# Register your models here.
admin.site.register(Bitcoin)
admin.site.register(Ethereum)
admin.site.register(Solana)
admin.site.register(RandomTweetBTC)
admin.site.register(RandomTweetETH)
admin.site.register(RandomTweetSOL)