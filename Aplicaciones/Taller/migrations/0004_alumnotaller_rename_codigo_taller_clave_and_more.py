# Generated by Django 4.2.6 on 2023-12-08 05:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Taller', '0003_alter_inscripciontaller_fechacompletado'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumnoTaller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInscripcion', models.DateTimeField(auto_now_add=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Taller.alumno')),
            ],
        ),
        migrations.RenameField(
            model_name='taller',
            old_name='codigo',
            new_name='clave',
        ),
        migrations.RemoveField(
            model_name='taller',
            name='ponente',
        ),
        migrations.AddField(
            model_name='taller',
            name='docente',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='InscripcionTaller',
        ),
        migrations.AddField(
            model_name='alumnotaller',
            name='taller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Taller.taller'),
        ),
    ]