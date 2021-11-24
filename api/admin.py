from django.contrib import admin
from .models import Bitcoin, Ethereum, Solana


# Register your models here.
admin.site.register(Bitcoin)
admin.site.register(Ethereum)
admin.site.register(Solana)