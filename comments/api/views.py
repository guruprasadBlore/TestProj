from  rest_framework import generics
from .comment_serializer import CommentSerializer
from ..models import Comments

class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self,*args,**kwargs):
        return Comments.objects.all()

