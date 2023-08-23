from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.


class Publicacion(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    titulo = models.CharField(max_length=50)
    # imagen
    contenido = models.CharField(max_length=2000)
    me_gusta =  models.IntegerField(default=0)
    publico = models.BooleanField(default=False)
    fecha_creacion  =  models.DateField(auto_now_add=True)
    fecha_actualizacion =  models.DateField(auto_now=True)
    status =  models.BooleanField(default=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.uuid} | {self.titulo}'


class Comentario(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    contenido = models.CharField(max_length=500)
    publicacion =  models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    me_gusta =  models.IntegerField(default=0)
    publico = models.BooleanField(default=False)
    fecha_creacion  =  models.DateField(auto_now_add=True)
    fecha_actualizacion =  models.DateField(auto_now=True)
    status =  models.BooleanField(default=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.uuid} | {self.publicacion}'