# Generated by Django 5.0.6 on 2024-06-26 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
