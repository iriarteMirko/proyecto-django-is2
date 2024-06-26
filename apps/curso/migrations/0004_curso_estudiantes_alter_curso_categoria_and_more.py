# Generated by Django 5.0.6 on 2024-06-24 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_remove_curso_calificacion_and_more'),
        ('estudiante', '0001_initial'),
        ('inscripcion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='estudiantes',
            field=models.ManyToManyField(through='inscripcion.Inscripcion', to='estudiante.estudiante'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='categoria',
            field=models.CharField(choices=[('Desarrollo', 'Desarrollo'), ('Negocios', 'Negocios'), ('Finanzas', 'Finanzas'), ('Contabilidad', 'Contabilidad'), ('Informática y Software', 'Informática y Software'), ('Productividad', 'Productividad'), ('Diseño', 'Diseño'), ('Marketing', 'Marketing'), ('Economía', 'Economía'), ('Administración', 'Administración'), ('Derecho', 'Derecho'), ('Gestión de Proyectos', 'Gestión de Proyectos')], max_length=100),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('Principiante', 'Principiante'), ('Intermedio', 'Intermedio'), ('Avanzado', 'Avanzado'), ('Experto', 'Experto')], max_length=100),
        ),
    ]
