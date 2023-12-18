from rest_framework import generics, permissions, filters
from friends_chats.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer

class VideoListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer