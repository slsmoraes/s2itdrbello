from django.shortcuts import render

from cadmediuns.models import CadastroMediuns

def cadmediuns_lista(request):
    listamediuns = CadastroMediuns.objects.all()
    return render(request, 'cadmediuns_lista.html', {'listamediuns': listamediuns})


