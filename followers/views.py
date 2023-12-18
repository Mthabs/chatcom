from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
