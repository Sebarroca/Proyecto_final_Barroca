# Generated by Django 4.1.3 on 2024-08-09 19:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0003_rename_profesion_profesor_especialidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='fecha',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='apellido',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Záéíóúñ]+$', 'No se permiten números.')]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Záéíóúñ]+$', 'No se permiten números.')]),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='apellido',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Záéíóúñ]+$', 'No se permiten números.')]),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='nombre',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Záéíóúñ]+$', 'No se permiten números.')]),
        ),
    ]
