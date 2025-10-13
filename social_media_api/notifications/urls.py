from django.urls import path
from .views import NotificationListView, MarkNotificationAsReadView, UnreadNotificationCountView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('notifications/<int:notification_id>/read/', MarkNotificationAsReadView.as_view(), name='mark_notification_as_read'),
    path('notifications/unread_count/', UnreadNotificationCountView.as_view(), name='unread_notification_count'),
]

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),
    path('<int:notification_id>/read/', MarkNotificationAsReadView.as_view(), name='mark_notification_as_read'),
    path('unread_count/', UnreadNotificationCountView.as_view(), name='unread_notification_count'),
]