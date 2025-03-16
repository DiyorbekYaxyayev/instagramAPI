from rest_framework import serializers
from instagram.models import Post, Comment


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostModelSerializer(serializers.ModelSerializer):
    comments = CommentModelSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'comments']

