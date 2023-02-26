# Generated by Django 4.1.1 on 2022-10-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_bikespot_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikespot',
            name='mid_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bikespot',
            name='mid_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
