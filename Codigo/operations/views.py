from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'operaciones/peticion.html')

def respuesta(request):
    simbolos = {
        'suma': '+',
        'resta': '-',
        'multiplicacion': '*'
    }

    operacion = request.POST['operacion']
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    respuesta = None
    if operacion == 'suma':
        respuesta = num1 + num2
    elif operacion == 'resta':
        respuesta = num1 - num2
    else:
        respuesta = num1 * num2

    context = {
        'operacion': operacion,
        'simbolo': simbolos[request.POST['operacion']],
        'num1': num1,
        'num2': num2,
        'respuesta': respuesta
    }
    return render(request, 'operaciones/respuesta.html', context)