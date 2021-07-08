# from django.shortcuts import render
from .models import Indexes
from .serializers import indexes_serializer
from rest_framework import generics , status
from rest_framework.views import APIView
from rest_framework.response import Response



class Indexes_list(APIView):
    def get(self, request):
        query = Indexes.objects.all()
        serializers = indexes_serializer(query, many =True)
        return Response(serializers.data , status=status.HTTP_200_OK)
    

class Index_info(APIView):
    def get(self , request , symbolISIN):
        query = Indexes.objects.filter(symbolISIN = symbolISIN)
        serializers = indexes_serializer(query, many =True)
        return Response(serializers.data , status=status.HTTP_200_OK)