from rest_framework import serializers
from ecommerce.models import post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ('title','user','content')
