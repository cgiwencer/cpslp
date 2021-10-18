from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('gestionUsuarios', views.usuarios),
    path('registrarUsuario', views.registrarUsuario),
    path('edicionUsuario/<codigo>', views.edicionUsuario),
    path('editarUsuario', views.editarUsuario),
    path('eliminarUsuario/<codigo>', views.eliminarUsuario),
    path('Agenda', views.agendatelefonica)
]