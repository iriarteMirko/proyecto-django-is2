# Generated by Django 5.0.6 on 2024-07-11 00:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrera', models.CharField(choices=[('Arquitectura', 'Arquitectura'), ('Administración', 'Administración'), ('Contabilidad y Finanzas', 'Contabilidad y Finanzas'), ('Economía', 'Economía'), ('Marketing', 'Marketing'), ('Negocios Internacionales', 'Negocios Internacionales'), ('Comunicación', 'Comunicación'), ('Derecho', 'Derecho'), ('Ingeniería Civil', 'Ingeniería Civil'), ('Ingeniería Industrial', 'Ingeniería Industrial'), ('Ingeniería de Sistemas', 'Ingeniería de Sistemas'), ('Psicología', 'Psicología')], max_length=25)),
                ('ciclo', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
    ]
