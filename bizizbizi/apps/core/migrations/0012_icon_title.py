# Generated by Django 4.1.1 on 2022-10-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_icon_end_flag_icon_start_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='icon',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]