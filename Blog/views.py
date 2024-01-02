from django.shortcuts import render

from rest_framework import viewsets


from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status


from .models import CategoryTable, PostViews,Comment
from .serializers import CategorySerializer, PostViewsSerializer,CommentSerializer

# Create your views here.

class CategoryMVS(viewsets.ModelViewSet):
    queryset = CategoryTable.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name']
    search_fields = ['title']


class PostViewsMVS(viewsets.ModelViewSet):
    queryset = PostViews.objects.all()
    serializer_class = PostViewsSerializer
    filterset_fields = ['category__name']
    search_fields = ['title']


class CommentMVS(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ['category__name']
    search_fields = ['title']

