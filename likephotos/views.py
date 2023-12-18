from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Likephoto
from .serializers import LikephotoSerializer

class LikephotoCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Likephoto.objects.all()
    serializer_class = LikephotoSerializer
    