# Generated by Django 4.0 on 2022-01-03 12:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('naissance_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nouveau_ne',
            name='situa_matri_mere',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='situation matrimoniale de la mere'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nouveau_ne',
            name='situ_matri_pere',
            field=models.CharField(max_length=100, verbose_name='situation matrimoniale du pere'),
        ),
    ]
