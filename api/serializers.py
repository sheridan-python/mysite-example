from rest_framework import serializers
from blog.models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'author',
            'published',
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    # Get the full name of the author
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'author',
            'author_full_name',
            'banner',
            'content',
            'published',
        ]

    def get_author_full_name(self, obj):
        """
        Returns the author's full name
        """
        return obj.author.get_full_name()
