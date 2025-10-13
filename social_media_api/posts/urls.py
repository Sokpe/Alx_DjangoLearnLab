from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CommentViewSet
from .views import FeedView
from .views import LikePostView, UnlikePostView

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

urlpatterns = [
    path('<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
]