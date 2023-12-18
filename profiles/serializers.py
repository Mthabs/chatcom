from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    
    class Meta:
        model = UserProfile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'name', 'content','is_owner', 'profile_picture', 'cover_photo']

    def to_representation(self, instance):
        if isinstance(instance, UserProfile):
            representation = super().to_representation(instance)
            default_profile_picture_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_yansvo.jpg'
            default_cover_photo_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_ifketo.jpg'
                
            if not instance.profile_picture:
                representation['profile_picture'] = default_profile_picture_url

            if not instance.cover_photo:
                representation['cover_photo'] = default_cover_photo_url

            return representation
        return {}

    def get_is_owner(self, obj):
        if isinstance(obj, UserProfile):
            request = self.context.get('request')
            return request.user == obj.owner
        return False