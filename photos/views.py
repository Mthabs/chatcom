from rest_framework import generics, permissions, filters
from friends_chats.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .models import Photo
from .serializers import PhotoSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class PhotoListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'caption',
    ]
    ordering_fields = [
        'like_count',
        'comment_count',
        'likephotos__created_at',
    ]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer