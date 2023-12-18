from django.urls import path
from .views import LikephotoCreateView 

urlpatterns = [
    path('likephotos/', LikephotoCreateView.as_view(), name='like-list-create'), 
]