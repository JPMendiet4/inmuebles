# Generated by Django 3.2 on 2023-02-12 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebleslist_app', '0002_rename_description_inmueble_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmueble',
            old_name='active',
            new_name='activo',
        ),
    ]
