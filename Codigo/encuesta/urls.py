from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('enviar', view=views.enviar, name='enviar')
]