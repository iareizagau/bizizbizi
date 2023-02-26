# Generated by Django 4.1.1 on 2022-10-02 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_gpstracks_color_alter_gpstracks_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.ImageField(blank=True, null=True, upload_to='img/icon')),
                ('end', models.ImageField(blank=True, null=True, upload_to='img/icon')),
                ('shadow', models.ImageField(blank=True, null=True, upload_to='img/icon')),
                ('bike', models.ImageField(blank=True, null=True, upload_to='img/icon')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Icon',
                'verbose_name_plural': 'Icons',
                'ordering': ['created'],
            },
        ),
    ]