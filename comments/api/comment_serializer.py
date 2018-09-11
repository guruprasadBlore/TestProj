from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from ..models import Comments

class CommentSerializer(ModelSerializer):
    user = SerializerMethodField()
    post = SerializerMethodField()
    class Meta:
        model = Comments
        fields = ('user','post','content','timestamp')

    def get_user(self,obj):
        return obj.user.username

    def get_post(self,obj):
        return obj.post.title
