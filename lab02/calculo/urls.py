from django.urls import path

from . import views

app_name = 'calculo'

urlpatterns = [
    path('', views.index, name='index'),
    path('tarea1/', views.tarea1, name='tarea1'),
    path('tarea2/', views.tarea2, name='tarea2'),
    path('enviar',views.enviar,name='enviar'),
    path('enviar2',views.enviar2,name='enviar2'),
]