
from django.urls import path

from . import views

urlpatterns = [
    path('', views.nazionale, name='nazionale'),
    path('lista_regioni', views.lista_regioni, name='lista_regioni'),
    path('lista_province', views.lista_province, name='lista_province'),
]
