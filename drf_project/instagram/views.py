from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer

from .serializers import PostSerializer
from .models import Post


class PublicPostListAPIView(APIView):
    def get(self, request, format=None):
        queryset = Post.objects.filter(is_public=True)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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