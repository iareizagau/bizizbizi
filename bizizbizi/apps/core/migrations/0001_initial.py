# Generated by Django 4.1.1 on 2022-10-01 15:21

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='BikeSpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('town', models.CharField(blank=True, max_length=200, null=True)),
                ('start_latitude', models.FloatField(blank=True, null=True)),
                ('start_longitude', models.FloatField(blank=True, null=True)),
                ('end_latitude', models.FloatField(blank=True, null=True)),
                ('end_longitude', models.FloatField(blank=True, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('image7', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('image8', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('gpx', models.BooleanField(blank=True, null=True, verbose_name='gpx')),
                ('auto_gpx', models.BooleanField(blank=True, null=True, verbose_name='auto_gpx')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.country')),
            ],
            options={
                'verbose_name': 'Geldialdia',
                'verbose_name_plural': 'Geldialdiak',
                'ordering': ['created'],
            },
        ),
    ]
