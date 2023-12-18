from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    