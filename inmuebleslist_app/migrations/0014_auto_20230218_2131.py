# Generated by Django 3.2 on 2023-02-18 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebleslist_app', '0013_auto_20230218_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacion',
            name='avg_calificacion',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='edificacion',
            name='number_calificacion',
            field=models.IntegerField(default=0),
        ),
    ]
