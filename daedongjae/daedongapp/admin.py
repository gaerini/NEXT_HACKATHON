from django.contrib import admin
from .models import Market, Group, Game, GameRoom
# Register your models here.

admin.site.register(Market)
admin.site.register(Group)
admin.site.register(Game)
admin.site.register(GameRoom)