from rest_framework import serializers
from .models import(Car)
from rest_framework.permissions import (IsAuthenticated)

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields='__all__'