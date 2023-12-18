from django.urls import path
from .views import FollowerListCreateView

urlpatterns = [
    path('followers/', FollowerListCreateView.as_view(), name='follower-list-create'),
]