from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CommentViewSet
from .views import FeedView

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    # existing routes...
    path('feed/', FeedView.as_view(), name='feed'),
]


urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]