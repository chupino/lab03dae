from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('calculo/', view=views.calculo, name='calculo')
]