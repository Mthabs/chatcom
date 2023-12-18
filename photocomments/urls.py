from django.urls import path
from .views import PhotocommentListCreateView

urlpatterns = [
    path('photocomments/', PhotocommentListCreateView.as_view(), name='photocomment-list-create'),
]