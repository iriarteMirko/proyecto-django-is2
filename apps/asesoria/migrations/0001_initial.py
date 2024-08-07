# Generated by Django 5.0.6 on 2024-07-17 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asesoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(help_text='Fecha de la asesoría')),
                ('hora_inicio', models.TimeField(help_text='Hora de inicio de la asesoría')),
                ('hora_fin', models.TimeField(help_text='Hora de fin de la asesoría')),
                ('enlace', models.URLField(help_text='Enlace de la reunión')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asesorias', to='curso.curso')),
            ],
            options={
                'verbose_name': 'Asesoría',
                'verbose_name_plural': 'Asesorías',
            },
        ),
    ]
