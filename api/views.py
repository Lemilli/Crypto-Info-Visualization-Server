from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.seralizers import BitcoinSerializer, EthereumSerializer, SolanaSerializer
from .models import Bitcoin, Ethereum, Solana

# Create your views here.
class GetBitcoin(APIView):
    def get(self, request):
        btc_data = Bitcoin.objects.all()
        serializer = BitcoinSerializer(btc_data, many=True)
        return Response(serializer.data)
        # return json
    
class GetEthereum(APIView):
    def get(self, request):
        eth_data = Ethereum.objects.all()
        serializer = EthereumSerializer(eth_data, many=True)
        return Response(serializer.data)
        # return json
    
class GetSolana(APIView):
    def get(self, request):
        sol_data = Solana.objects.all()
        serializer = SolanaSerializer(sol_data, many=True)
        return Response(serializer.data)
        # return json
    
