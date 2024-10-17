from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contactos, name='lista_contactos'),
    path('cargar_contactos/', views.cargar_contactos, name='cargar_contactos'),
]
