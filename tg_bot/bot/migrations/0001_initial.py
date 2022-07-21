# Generated by Django 4.0.6 on 2022-07-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_tg_id', models.BigIntegerField(db_index=True, unique=True)),
                ('state_name', models.CharField(max_length=255)),
                ('context', models.JSONField(default=dict)),
            ],
            options={
                'db_table': 'BotState',
            },
        ),
    ]