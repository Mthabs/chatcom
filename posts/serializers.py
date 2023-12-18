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

        