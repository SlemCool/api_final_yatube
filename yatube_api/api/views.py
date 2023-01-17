from rest_framework import filters, status, viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from .permissions import IsOwnerOrReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from posts.models import Follow, Group, Post, User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(status.HTTP_403_FORBIDDEN)
        instance.delete()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# class FollowViewSet(viewsets.ModelViewSet):
#     serializer_class = FollowSerializer
#     permission_classes = (permissions.IsAuthenticated,) 
#     filter_backends = (filters.SearchFilter)
#     search_fields = ('following__username',)
#     def get_queryset(self):
#         # return self.request.user.followers.all()
#         return Follow.objects.filter(user=self.request.user)

class FollowViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]
    permission_classes = (permissions.IsAuthenticated)

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        # if serializer.instance.user != self.request.user:
        #     raise PermissionDenied('Изменение чужого контента запрещено!')
        user = self.request.user
        serializer.save(user=user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        return post.comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(status.HTTP_403_FORBIDDEN)
        instance.delete()
