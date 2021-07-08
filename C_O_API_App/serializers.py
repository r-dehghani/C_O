from rest_framework import serializers
from .models import Indexes

class indexes_serializer(serializers.ModelSerializer):
    class Meta:
        model = Indexes
        fields = "__all__"

