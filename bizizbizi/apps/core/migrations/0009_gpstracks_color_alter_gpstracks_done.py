# Generated by Django 4.1.1 on 2022-10-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_warmshower_done_gpstracks_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpstracks',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gpstracks',
            name='done',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
