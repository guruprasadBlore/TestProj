from rest_framework import generics
from django.db.models import Q
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

from .MySerializer import PostSerializer
from ecommerce.pagination import CustomPagePaginator
from ..models import post
from .permission import IsOwner


class PostListApiView(generics.ListAPIView):
    # authentication_classes = (BasicAuthentication,)
    #model = post
    serializer_class = PostSerializer
    pagination_class = CustomPagePaginator
    def get_queryset( self ):
        queryset_list = post.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__contains=query)
            ).distinct()
        return queryset_list


class CreatePostFromApi(generics.CreateAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReterivePostFromAPI(generics.RetrieveAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    # lookup_url_kwarg = 'slug'

class UpdatePostFromAPI(generics.RetrieveUpdateAPIView):
    queryset = post.objects.all()
    permission_classes = [IsAuthenticated,IsOwner]
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class DeletePostFromAPI(generics.DestroyAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'






