from rest_framework import serializers
from .models import indexes , trigger , make_deal

class indexes_serializer(serializers.ModelSerializer):
    class Meta:
        model = indexes
        fields = "__all__"

class trigger_serializer(serializers.ModelSerializer):
    class Meta:
        model = trigger
        fields = "__all__"