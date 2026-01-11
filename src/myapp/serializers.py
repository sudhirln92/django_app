from rest_framework import serializers
from .models import *


class ExternaltokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Externaltoken
        fields = "__all__"

    def create(self, validated_data):
        return Externaltoken.objects.create(**validated_data)
