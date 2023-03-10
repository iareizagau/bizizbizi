# Generated by Django 4.1.5 on 2023-02-24 11:28

import apps.registration.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=apps.registration.models.custom_upload_to)),
                ('bio', models.TextField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('mountain_club', models.CharField(blank=True, max_length=200, null=True, verbose_name='Mendi elkartea')),
                ('public', models.BooleanField(blank=True, null=True, verbose_name='Erabiltzaile publikoa')),
                ('log_count', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Saioa hasi kontadorea')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sortze data')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Edizio data')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profila',
                'verbose_name_plural': 'Profilak',
                'ordering': ['user__username'],
            },
        ),
    ]
