# Generated by Django 4.1.1 on 2022-10-08 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_pointsinterest_youtube'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gpstracks',
            old_name='gpx',
            new_name='gpx_path',
        ),
    ]
