from rest_framework import generics, permissions, filters
from friends_chats.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .models import Photo
from .serializers import PhotoSerializer


class PhotoListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
