from django.contrib import admin
from .models import Team, Player


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'location',
        'slug',
        'date_updated'
    ]

    prepopulated_fields = {
        'slug': ('name', )
    }


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = [
        'team',
        'first_name',
        'last_name',
        'patronymic',
        'goals',
        'assists',
        'yellow_cards',
        'red_cards',
        'status',
        'date_updated',
    ]

    list_editable = [
        'goals',
        'assists',
        'yellow_cards',
        'red_cards',
        'status'
    ]

    prepopulated_fields = {
        'slug': ('team', 'first_name', 'last_name', 'patronymic',)
    }

    list_display_links = [
        'team',
    ]
