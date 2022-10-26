from django.contrib import admin

from bot import models


@admin.register(models.BotState)
class BotStateAdmin(admin.ModelAdmin):
    pass
