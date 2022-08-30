from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "user_id", "title", "body" ]


class PostSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "body" ]