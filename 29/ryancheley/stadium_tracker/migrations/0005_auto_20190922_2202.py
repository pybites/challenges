# Generated by Django 2.2.2 on 2019-09-22 22:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stadium_tracker', '0004_auto_20190919_0229'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='gamedetails',
            unique_together={('user', 'game_id')},
        ),
    ]
