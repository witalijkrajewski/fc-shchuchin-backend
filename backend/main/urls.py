from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.TeamList.as_view()),
    path('players/', views.PlayerList.as_view()),

]
