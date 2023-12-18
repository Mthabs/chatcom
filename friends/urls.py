from django.urls import path
from .views import FriendListCreateView

urlpatterns = [
    path('friends/', FriendListCreateView.as_view(), name='friend-list-create'),
]