from rest_framework import serializers

from .models import Circular

class CircularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circular
        fields = '__all__'