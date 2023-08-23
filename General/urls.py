from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('publicacion/<uuid:uuid>/ver', VerPublicacion.as_view(), name='ver_publicacion'),
    path('publicacion/<uuid:uuid>/like', AddPublicacionLike.as_view(), name='add_publicacion_like'),
]