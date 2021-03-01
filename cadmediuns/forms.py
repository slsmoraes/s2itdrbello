from django.forms import ModelForm
from .models import CadastroMediuns

class CadastroMediunsForm(ModelForm):
    class Meta:
        model = CadastroMediuns
        fields = ['nome',
                  'endereco',
                  'email',
                  'data_nascimento',
                  'celular',
                  'fixo',]