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


    def validate_image(self, value):
        # Check file size
        max_size = 3 * 1024 * 1024  # Maximum size allowed (2MB)

        if value.size > max_size:
            raise serializers.ValidationError(f"File size too large. Max size is {max_size} bytes.")

        return value

    