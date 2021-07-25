# from django.shortcuts import render
from .models import indexes , trigger
from .serializers import indexes_serializer , trigger_serializer
from rest_framework import generics , status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

# from .producer import publish

class indexes_list(APIView):
    def get(self, request):
        query = indexes.objects.all()
        serializers = indexes_serializer(query, many =True)
        # publish("indexes_called" , serializers.data)
        return Response(serializers.data , status=status.HTTP_200_OK)
    

class index_info(APIView):
    def get(self , request , symbolisin):
        query = indexes.objects.filter(symbolisin = symbolisin)
        serializers = indexes_serializer(query, many =True)
        # publish("index_called" , serializers.data)
        return Response(serializers.data , status=status.HTTP_200_OK)

class browse_symbol(APIView):
    
    def post(self, request):
        serializers = trigger_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        
        # publish("indexes_called" , serializers.data)
        
        # user_symbol = serializers.data.get('user_symbol')
        # oper = serializers.data.get('oper')
        # desired_price = serializers.data.get('desired_price')
        
        # trigger1 = trigger()
        # trigger1.user_symbol = user_symbol
        # trigger1.oper = oper
        # trigger1.desired_price = desired_price
        # trigger1.save()
        return Response(serializers.data , status = status.HTTP_201_CREATED)
