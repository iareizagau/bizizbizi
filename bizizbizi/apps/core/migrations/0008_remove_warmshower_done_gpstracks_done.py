# Generated by Django 4.1.1 on 2022-10-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_gpstracks_options_warmshower_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warmshower',
            name='done',
        ),
        migrations.AddField(
            model_name='gpstracks',
            name='done',
            field=models.BooleanField(blank=True, null=True, verbose_name='gpx'),
        ),
    ]
