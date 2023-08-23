from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import *
# Create your views here.


class Home(View):
    def get(self, request):
        publicaciones =  Publicacion.objects.filter(publico = True)
        return render(request, 'common/home.html', { 'publicaciones': publicaciones})
    

class AddPublicacionLike(View):
    def post(self, request, uuid):
        publicacion =  Publicacion.objects.get(uuid = uuid)
        publicacion.me_gusta = publicacion.me_gusta + 1
        publicacion.save()   

        return HttpResponseRedirect(reverse('home'))


class VerPublicacion(View):
    def get(self, request, uuid):
        publicacion =  Publicacion.objects.get(uuid = uuid)
        comentarios =  Comentario.objects.filter(publicacion = publicacion)

        return render(request, 'publicaciones/ver_publicacion.html', {'publicacion':publicacion, 'comentarios': comentarios})
