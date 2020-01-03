from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from main_app.models import Post, Comment
from main_app.serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Post model.
    Actions: All
    """

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=True, url_path="comments")
    def get_comments(self, request, pk):
        comments = Comment.objects.filter(post=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentViewSet(
    viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
):
    """
    ViewSet for Comment model.
    Actions: View, Update, Delete
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
