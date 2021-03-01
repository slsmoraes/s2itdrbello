from django.shortcuts import render, redirect

from cadmediuns.models import CadastroMediuns
from cadmediuns.forms import CadastroMediunsForm

def cadmediuns_lista(request):
    listamediuns = CadastroMediuns.objects.all()
    return render(request, 'cadmediuns_lista.html', {'listamediuns': listamediuns})

def cadmediuns_insert(request):
    form = CadastroMediunsForm(request.POST, None)
    if form.is_valid():
        form.save()
        return redirect('cadmediuns_lista')
    return render(request, 'cadmediuns.html', {'form': form})
