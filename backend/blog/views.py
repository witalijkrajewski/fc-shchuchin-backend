from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogMainTheme, Blog
from .serializes import MainThemeSerializer, BlogSerializer
from django.shortcuts import render, get_object_or_404


class BlogThemesList(APIView):
    def get(self, request, format=None):
        themes = BlogMainTheme.objects.all()
        serializer = MainThemeSerializer(themes, many=True)
        return Response(serializer.data)


class Blogs(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
