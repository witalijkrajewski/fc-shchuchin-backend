from django.contrib import admin
from .models import Blog, BlogMainTheme


@admin.register(BlogMainTheme)
class BlogMainThemeAdmin(admin.ModelAdmin):
    list_display = [
        'main_theme',
        'slug'
    ]

    list_editable = [
        'slug'
    ]

    prepopulated_fields = {
        'slug': ('main_theme',)
    }


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'theme',
        'title',
    ]

    list_editable = [
        'title'
    ]

    prepopulated_fields = {
        'slug': ('theme', 'title')
    }
