from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Photocomment
from .serializers import PhotocommentSerializer

class PhotocommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Photocomment.objects.all()
    serializer_class = PhotocommentSerializer