from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Photocomment
from .serializers import PhotocommentSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class PhotocommentListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Photocomment.objects.all()
    serializer_class = PhotocommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['photo']
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PhotocommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Photocomment.objects.all()
    serializer_class = PhotocommentSerializer