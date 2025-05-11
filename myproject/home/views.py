from django.shortcuts import render
from .models import Bhaskara
import math

# Create your views here.
def render_home(request):
    return render(request, 'home/index.html')


def calcular_baskhara(request):
    if request.method == 'POST':
        resultado = []
        try:
            bask = Bhaskara()
            bask.a = float(request.POST.get('a'))
            bask.b = float(request.POST.get('b'))
            bask.c = float(request.POST.get('c'))

            bask.delta = bask.b**2 - 4*bask.a*bask.c

            if bask.delta < 0:
                resultado = ['Não existem raízes reais.']

            elif bask.delta == 0:
                x = -bask.b / (2*bask.a)
                bask.x1 = x
                bask.x2 = x
                resultado = [x]
                bask.save()

            else:
                bask.x1 = (-bask.b + math.sqrt(bask.delta)) / (2*bask.a)
                bask.x2 = (-bask.b - math.sqrt(bask.delta)) / (2*bask.a)
                resultado = [bask.x1, bask.x2]
                bask.save()

        except (TypeError, ValueError):
            resultado = ['Erro: insira apenas números válidos.']

        except:
            resultado = ['Erro: nao foi possivel concluir a operacao.']

        return render(request, 'home/index.html', {'result':resultado})
    return render(request, 'home/index.html')


def lista_bhaskaras(request):
    bhaskaras = Bhaskara.objects.all().order_by('-id')
    return render(request, 'home/table.html', {'bhaskaras': bhaskaras})


def deleta_bhaskaras(request):
    return render(request, 'home/table.html')
