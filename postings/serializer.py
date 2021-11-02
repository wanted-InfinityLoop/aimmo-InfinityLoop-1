from django.db.models import fields
from .models import Comment, Posting
from rest_framework import serializers


class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = ["title", "text"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]

class PostingListQuerySerializer(serializers.ModelSerializer):
    offset   = serializers.IntegerField(help_text="offset", required=False)
    limit    = serializers.IntegerField(help_text="limit", required=False)
    category = serializers.CharField(help_text="category", required=True)
    title = serializers.CharField(help_text="title", required=False)
    username = serializers.CharField(help_text="username", required=False)