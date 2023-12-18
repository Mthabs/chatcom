from django.db.models import Count
from rest_framework import generics, permissions, filters
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = UserProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'name',
        'content',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]

    def get_queryset(self):
        queryset = UserProfile.objects.annotate(
            posts_count=Count('owner__posts', distinct=True),
            followers_count=Count('owner__following', distinct=True),  
            following_count=Count('owner__followed', distinct=True)    
        )
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        existing_profile = UserProfile.objects.filter(owner=user).first()
        if existing_profile:
            serializer.update(existing_profile, serializer.validated_data)
        else:
            serializer.save(owner=user)


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = UserProfileSerializer 
    def get_queryset(self):
        queryset = UserProfile.objects.annotate(
            posts_count=Count('owner__posts', distinct=True),
            followers_count=Count('owner__following', distinct=True),  
            following_count=Count('owner__followed', distinct=True)   
        )
        return queryset