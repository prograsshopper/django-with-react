from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly


class PublicPostListAPIView(APIView):
    def get(self, request, format=None):
        queryset = Post.objects.filter(is_public=True)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['message']
    ordering_fields = ['pk']
    ordering = ['pk']

    def perform_create(self, serializer):
        author = self.request.user # User pr AnonymousUser
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(author=author, ip=ip)

    @action(detail=False, methods=['GET'])
    def public(self, request):
        queryset = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)        


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "instagram/post_detail.html"

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({
            'post': post,
        })