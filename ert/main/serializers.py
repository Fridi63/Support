from .models import Support
from rest_framework import serializers


class SupportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Support
        fields = ('short_descriptions', 'detailed_description', 'email')


class CreateUser(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=20)
