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

    @action(detail=True, url_path="comments/create", methods=["post"])
    def create_comments(self, request, pk):
        serializer = CommentSerializer(many=True, data=request.data)
        if serializer.is_valid():
            comments = serializer.save()
            self.get_object().comments.add(*comments)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(
    viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
):
    """
    ViewSet for Comment model.
    Actions: View, Update, Delete
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
