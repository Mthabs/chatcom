from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = UserProfile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'name', 'content', 'profile_picture', 'cover_photo']