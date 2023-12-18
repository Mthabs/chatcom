from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Videocomment
from .serializers import VideocommentSerializer

class VideocommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Videocomment.objects.all()
    serializer_class = VideocommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VideocommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Videocomment.objects.all()
    serializer_class = VideocommentSerializer