from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Likephoto
from .serializers import LikephotoSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class LikephotoCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Likephoto.objects.all()
    serializer_class = LikephotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikephotoUnlikeView(generics.RetrieveDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Likephoto.objects.all()
    serializer_class = LikephotoSerializer
    