from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class LikeListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeUnlikeView(generics.RetrieveDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer