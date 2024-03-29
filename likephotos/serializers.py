from rest_framework import serializers
from django.db import IntegrityError, transaction
from .models import Likephoto

class LikephotoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Likephoto
        fields = ['id', 'photo', 'owner', 'created_at']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"error" : "You have already liked this photo."})