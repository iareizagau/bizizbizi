# Generated by Django 4.1.1 on 2022-10-02 12:35

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_bikespot_options_alter_bikespot_image1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GpsTracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('town', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('gpx', models.FileField(upload_to='gpx')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='img/gps_track')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='img/gps_track')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='img/gps_track')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='img/gps_track')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='img/gps_track')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='img/gps_track')),
                ('image7', models.ImageField(blank=True, null=True, upload_to='img/gps_track')),
                ('image8', models.ImageField(blank=True, null=True, upload_to='img/gps_track')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.country')),
            ],
            options={
                'verbose_name': 'Warmshower',
                'verbose_name_plural': 'Warmshowers',
                'ordering': ['created'],
            },
        ),
    ]
