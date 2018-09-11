"""My_Proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from ecommerce.views import welcome, post_list, post_detail,post_create, post_update, \
    post_api_view,logout_view
from ecommerce.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    url(r'^$', post_list),
    url(r'^api/posts/',include('ecommerce.api.urls')),
    url(r'^api/comments/',include('comments.api.urls')),
    url(r'^list', post_list),
    url(r'^admin/', admin.site.urls),
    url(r'login/$', welcome, name='login'),
    url(r'logout/$', logout_view, name='logout'),
    # url(r'^create/', post_create, name="create"),
    url(r'^cbv/', PostListView.as_view(), name='cbv'),
    url(r'^cbvdetail/(?P<pk>\d+)$', PostDetailView.as_view(), name='cbvdtl'),
    url(r'^cbvcreate/', PostCreateView.as_view(), name='cbvcreate'),
    url(r'cbvupdate/(?P<slug>[\w-]+)/', PostUpdateView.as_view(), name='cbvupdate'),
    url(r'cbvdelete/(?P<slug>[\w-]+)/', PostDeleteView.as_view(), name='cbvdelete'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)