from rest_framework import generics
from api import serializers
from .models import Post
from django.contrib.auth.models import User

class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = serializers.UserSerializer


class PostList(generics.ListCreateAPIView):
  """
  Handler for `get` and `post` for a list of posts
  """
  queryset = Post.objects.all()
  serializer_class = serializers.PostSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  Handler for `get`, `update`, and `delete` for a post
  """
  queryset = Post.objects.all()
  serializer_class = serializers.PostSerializer