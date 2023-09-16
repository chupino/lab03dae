from django.shortcuts import render
import math

# Create your views here.
def index(request):
    return render(request=request, template_name='index.html')

def calculo(request):
    diametro = float(request.POST['diametro'])
    altura = float(request.POST['altura'])
    radio = diametro / 2
    volumen = math.pi * radio**2 * altura

    return render(request=request, template_name='respuesta.html', context={'volumen': volumen})
