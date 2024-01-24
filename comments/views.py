from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CommentListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer   