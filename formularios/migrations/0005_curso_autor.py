# Generated by Django 4.1.3 on 2024-08-09 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formularios', '0004_curso_fecha_alter_estudiante_apellido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
