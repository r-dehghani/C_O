from rest_framework import serializers
from .models import indexes

class indexes_serializer(serializers.ModelSerializer):
    class Meta:
        model = indexes
        fields = "__all__"

