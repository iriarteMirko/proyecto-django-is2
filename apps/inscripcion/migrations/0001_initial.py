# Generated by Django 5.0.6 on 2024-07-17 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curso', '0001_initial'),
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscripciones', to='curso.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscripciones', to='estudiante.estudiante')),
            ],
            options={
                'verbose_name': 'Inscripción',
                'verbose_name_plural': 'Inscripciones',
                'unique_together': {('curso', 'estudiante')},
            },
        ),
    ]
