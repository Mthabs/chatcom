from .models import Post
from PIL import Image
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_picture = serializers.ReadOnlyField(source='user.userprofile.profile_picture_url')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'profile_id', 'owner', 'header', 'content', 'created_at', 'updated_at','profile_picture', 'post_picture', 'is_owner', 'image_filter']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        default_post_picture_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_post_wv7bvz.jpg'
        default_profile_picture_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_yansvo.jpg'

        if not instance.post_picture:
            representation['post_picture'] = default_post_picture_url

        if 'profile_picture' not in representation:
            representation['profile_picture'] = default_profile_picture_url

        return representation    