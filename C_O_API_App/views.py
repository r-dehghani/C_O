# from django.shortcuts import render
from .models import indexes
from .serializers import indexes_serializer
from rest_framework import generics , status
from rest_framework.views import APIView
from rest_framework.response import Response

from .producer import publish
class indexes_list(APIView):
    def get(self, request):
        query = indexes.objects.all()
        serializers = indexes_serializer(query, many =True)
        publish()
        return Response(serializers.data , status=status.HTTP_200_OK)
    

class index_info(APIView):
    def get(self , request , symbolisin):
        query = indexes.objects.filter(symbolisin = symbolisin)
        serializers = indexes_serializer(query, many =True)
        publish("index_called" , serializers.data)
        return Response(serializers.data , status=status.HTTP_200_OK)