from django.urls import path
from . import views

urlpatterns = [
    path('blog_themes/', views.BlogThemesList.as_view()),
    path('blogs/', views.Blogs.as_view()),
]
