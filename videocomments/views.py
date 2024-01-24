from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Videocomment
from .serializers import VideocommentSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class VideocommentListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Videocomment.objects.all()
    serializer_class = VideocommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['video']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VideocommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Videocomment.objects.all()
    serializer_class = VideocommentSerializer