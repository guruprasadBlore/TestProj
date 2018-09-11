from django.conf.urls import url,include
from .views import (
    PostListApiView,
    CreatePostFromApi,
    ReterivePostFromAPI,
    UpdatePostFromAPI,
    DeletePostFromAPI
)

urlpatterns = [
    url(r'^$', PostListApiView.as_view()),
    url(r'^create/$', CreatePostFromApi.as_view(), name='CreateApi'),
    url(r'^reterive/(?P<slug>[\w-]+)/$', ReterivePostFromAPI.as_view(), name='ReteriveApi'),
    url(r'^update/(?P<slug>[\w-]+)/$', UpdatePostFromAPI.as_view(), name='UpdateApi'),
    url(r'^delete/(?P<slug>[\w-]+)/$', DeletePostFromAPI.as_view(), name='DeleteApi'),
    ]