from rest_framework import serializers

from main_app.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for the Comment model."""

    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model."""

    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        # save comments
        comments = None
        if "comments" in validated_data:
            comments_data = validated_data.pop("comments")
            comments_serializer = CommentSerializer(many=True, data=comments_data)
            if comments_serializer.is_valid():
                comments = comments_serializer.save()
        post = Post.objects.create(**validated_data)
        if comments:
            post.comments.set(comments)
        return post
