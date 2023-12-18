from django.urls import path
from .views import VideocommentListCreateView

urlpatterns = [
    path('videocomments/', VideocommentListCreateView.as_view(), name='videocomment-list-create'),
]