from django.db import models


class BotState(models.Model):
    class Meta:
        db_table = 'BotState'

    user_tg_id = models.BigIntegerField(
        unique=True,
        db_index=True,
    )

    state_name = models.CharField(
        max_length=255
    )

    context = models.JSONField(default=dict)
