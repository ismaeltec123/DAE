from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'titulo':'Formulario',
    }
    return render(request,'calculo/index.html',context)

def tarea1(request):
    context={
        'titulo':'Tarea1',
    }
    return render(request,'calculo/formulario.html',context)

def tarea2(request):
    context={
        'titulo':'Tarea2',
    }
    return render(request,'calculo/form2.html',context)

def enviar (request):
    num1 = int(request.POST['numero1'])
    num2 = int(request.POST['numero2'])
    operacion= request.POST['operacion']
    signo=''
    if operacion == 'suma':
        resultado = num1 + num2
        signo='+'
    elif operacion == 'resta':
        resultado = num1 - num2
        signo='-'
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
        signo='*'
    elif operacion == 'division':
        resultado = num1 / num2
        signo='/'
    context = {
        'titulo': "Resultado",
        'num1': num1,
        'num2': num2,
        'operacion': request.POST['operacion'],
        'resultado': resultado,
        'signo': signo
    }
    return render (request, 'calculo/respuesta.html', context)
    
def enviar2 (request):
    diam = int(request.POST['diametro'])
    altura = int(request.POST['altura'])
    resultado=3.14*pow((diam/2),2)*altura
    context = {
        'titulo': "CALCULO DEL VOLUMEN DE UN CILINDRO",
        'Diametro': diam,
        'Altura': altura,
        'resultado': resultado,
    }
    return render (request, 'calculo/resultado.html', context)