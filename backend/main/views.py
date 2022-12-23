from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer
from django.shortcuts import render, get_object_or_404


class TeamList(APIView):
    def get(self, request, format=None):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


class PlayerList(APIView):
    def get(self, request, format=None):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
