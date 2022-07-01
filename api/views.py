from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.seralizers import BitcoinSerializer, EthereumSerializer, SolanaSerializer, RandomTweetBTCSerializer, RandomTweetETHSerializer, RandomTweetSOLSerializer
from .models import Bitcoin, Ethereum, Solana, RandomTweetBTC, RandomTweetETH, RandomTweetSOL

# Create your views here.
class GetBitcoin(APIView):
    def get(self, request):
        btc_data = Bitcoin.objects.all().order_by('-id')[:9000:-1]
        serializer = BitcoinSerializer(btc_data, many=True)
        return Response(serializer.data, headers={
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, DELETE',
            "Access-Control-Max-Age" : "86400",
            "Access-Control-Allow-Headers" : "X-Requested-With, Content-Type",
        })
        # return json
    
class GetEthereum(APIView):
    def get(self, request):
        eth_data = Ethereum.objects.all().order_by('-id')[:9000:-1]
        serializer = EthereumSerializer(eth_data, many=True)
        return Response(serializer.data, headers={
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, DELETE',
            "Access-Control-Max-Age" : "86400",
            "Access-Control-Allow-Headers" : "X-Requested-With, Content-Type",
        })
        # return json
    
class GetSolana(APIView):
    def get(self, request):
        sol_data = Solana.objects.all().order_by('-id')[:9000:-1]
        serializer = SolanaSerializer(sol_data, many=True)
        return Response(serializer.data, headers={
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, DELETE',
        })
        # return json
    
class GetRandomTweetBTC(APIView):
    def get(self, request):
        data = RandomTweetBTC.objects.all()
        serializer = RandomTweetBTCSerializer(data, many=True)
        return Response(serializer.data, headers={
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, DELETE',
            "Access-Control-Max-Age" : "86400",
            "Access-Control-Allow-Headers" : "X-Requested-With, Content-Type",
        })

class GetRandomTweetETH(APIView):
    def get(self, request):
        data = RandomTweetETH.objects.all()
        serializer = RandomTweetETHSerializer(data, many=True)
        return Response(serializer.data, headers={
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, DELETE',
            "Access-Control-Max-Age" : "86400",
            "Access-Control-Allow-Headers" : "X-Requested-With, Content-Type",
        })

class GetRandomTweetSOL(APIView):
    def get(self, request):
        data = RandomTweetSOL.objects.all()
        serializer = RandomTweetSOLSerializer(data, many=True)
        return Response(serializer.data, headers={
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, DELETE',
            "Access-Control-Max-Age" : "86400",
            "Access-Control-Allow-Headers" : "X-Requested-With, Content-Type",
        })

