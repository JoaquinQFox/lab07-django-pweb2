from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lista_destinos", views.lista_destinos, name="lista_destinos"),
    path("eliminar_destino/<int:id>/", views.eliminar_destino, name="eliminar_destino"),
    path("editar_destino/<int:id>/", views.editar_destino, name="editar_destino"),
    path("crear_destino", views.crear_destino, name="crear_destino"),
]