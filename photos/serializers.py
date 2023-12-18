from .models import Photo
from PIL import Image
from rest_framework import serializers
import cloudinary.uploader

class PhotoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = ['id', 'owner', 'image', 'caption', 'created_at', 'updated_at', 'is_owner']