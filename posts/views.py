from rest_framework import generics, permissions, filters
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer

class PostListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
