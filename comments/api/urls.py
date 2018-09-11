from django.conf.urls import url
from .views import CommentListAPIView

urlpatterns=[
    url(r'^$',CommentListAPIView.as_view(),name='comment-list')
]