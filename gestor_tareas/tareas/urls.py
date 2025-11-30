from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('tarea/<int:id>/', views.detalle_tarea, name='detalle_tarea'),
    path('tarea/agregar/', views.agregar_tarea, name='agregar_tarea'),
    path('tarea/eliminar/<int:id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
]
