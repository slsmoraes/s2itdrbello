from django.shortcuts import render, redirect, get_object_or_404

from cadmediuns.models import CadastroMediuns
from cadmediuns.forms import CadastroMediunsForm

def cadmediuns_lista(request):
    listamediuns = CadastroMediuns.objects.all()
    return render(request, 'cadmediuns_lista.html', {'listamediuns': listamediuns})

def cadmediuns_insert(request):
    form = CadastroMediunsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cadmediuns_lista')
    return render(request, 'cadmediuns.html', {'form': form})

def cadmediuns_update(request, id):
    cadmediuns = get_object_or_404(CadastroMediuns, pk=id)
    form = CadastroMediunsForm(request.POST or None, request.FILES or None, instance=cadmediuns)
    if form.is_valid():
        form.save()
        return redirect('cadmediuns_lista')
    return render(request, 'cadmediuns.html', {'form': form})

def cadmediuns_delete(request, id):
    cadmediuns = get_object_or_404(CadastroMediuns, pk=id)

    if request.method == 'POST':
        cadmediuns.delete()
        return redirect('cadmediuns_lista')
    return render(request, 'cadmediuns_delete_confirm.html', {'cadmediuns': cadmediuns})