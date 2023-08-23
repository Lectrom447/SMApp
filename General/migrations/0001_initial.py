# Generated by Django 4.2.4 on 2023-08-01 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=2000)),
                ('me_gusta', models.IntegerField(default=0)),
                ('publico', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('contenido', models.CharField(max_length=500)),
                ('me_gusta', models.IntegerField(default=0)),
                ('publico', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.publicacion')),
            ],
        ),
    ]