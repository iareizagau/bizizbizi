# Generated by Django 4.1.1 on 2022-10-02 12:14

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_bikespot_mid_latitude_bikespot_mid_longitude'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bikespot',
            options={'ordering': ['order'], 'verbose_name': 'Stage', 'verbose_name_plural': 'Stages'},
        ),
        migrations.AlterField(
            model_name='bikespot',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='img/stage'),
        ),
        migrations.AlterField(
            model_name='bikespot',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='img/stage'),
        ),
        migrations.AlterField(
            model_name='bikespot',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='img/stage'),
        ),
        migrations.AlterField(
            model_name='bikespot',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='img/stage'),
        ),
        migrations.AlterField(
            model_name='bikespot',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='img/stage'),
        ),
        migrations.AlterField(
            model_name='bikespot',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='img/stage'),
        ),
        migrations.AlterField(
            model_name='bikespot',
            name='image7',
            field=models.ImageField(blank=True, null=True, upload_to='img/stage'),
        ),
        migrations.AlterField(
            model_name='bikespot',
            name='image8',
            field=models.ImageField(blank=True, null=True, upload_to='img/stage'),
        ),
        migrations.CreateModel(
            name='Warmshower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('town', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='img/warmshower')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='img/warmshower')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='img/warmshower')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='img/warmshower')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='img/warmshower')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='img/warmshower')),
                ('image7', models.ImageField(blank=True, null=True, upload_to='img/warmshower')),
                ('image8', models.ImageField(blank=True, null=True, upload_to='img/warmshower')),
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
