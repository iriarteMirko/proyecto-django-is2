# Generated by Django 5.0.6 on 2024-05-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo electrónico')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('usuario_activo', models.BooleanField(default=True, verbose_name='Usuario activo')),
                ('usuario_administrador', models.BooleanField(default=False, verbose_name='Usuario administrador')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
