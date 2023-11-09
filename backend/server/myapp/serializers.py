from rest_framework import serializers
from .models import Post, CrashPadPost


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')

class CreatePostSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Post
        fields = ('caption', 'image', 'created_at', 'author_id')

class CrashPadPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrashPadPost
        fields = ('__all__')

class CreateCrashPadPostSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = CrashPadPost
        fields = ('text', 'location', 'created_at', 'author_id')

