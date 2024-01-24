from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Friend
from .serializers import FriendSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class FriendListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)   


class FriendUnfriendView(generics.RetrieveDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    