
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', render_home, name='index'),
    path('calcular_baskhara/', calcular_baskhara, name='calcular_baskhara'),
    path('resultados/', lista_bhaskaras, name='lista_bhaskaras'),
    path('resultados/delete', deleta_bhaskaras, name='deleta_bhaskaras'),
]
