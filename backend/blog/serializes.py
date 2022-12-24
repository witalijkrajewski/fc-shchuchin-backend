from rest_framework import serializers
from .models import BlogMainTheme, Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog

        fields = (
            'id',
            'theme',
            'title',
            'text',
            'get_blog_image',
            'get_blog_thumbnail',
            'date_created',
            'get_absolute_url',
        )


class MainThemeSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True)

    class Meta:
        model = BlogMainTheme

        fields = (
            'id',
            'main_theme',
            'blogs',
            'get_absolute_url'
        )

