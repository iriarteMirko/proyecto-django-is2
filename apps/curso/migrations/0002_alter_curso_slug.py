# Generated by Django 5.0.6 on 2024-07-10 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
