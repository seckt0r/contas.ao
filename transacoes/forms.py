from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Transacao, Categoria, Entidade, Conta


class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = '__all__'

        widgets = {
            'data': forms.DateTimeInput(
                attrs={
                    'id': 'data',
                    'type': 'hidden'
                }
            ),

            'tipo': forms.Select(
                attrs={
                    'id': 'tipo',
                    'required': True
                }
            ),
            'valor': forms.NumberInput(
                attrs={
                    'id': 'valor',
                    'required': True
                }
            ),
            'id_categoria': forms.Select(
                attrs={
                    'id': 'id_categoria',
                    'required': True
                }
            ),
            'id_origem': forms.Select(
                attrs={
                    'id': 'id_origem',
                    'required': True
                }
            ),
            'id_destino': forms.Select(
                attrs={
                    'id': 'id_destino',
                    'required': True
                }
            ),

        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'id': 'nome',
                    'required': True
                }
            ),
        }       

class EntidadeForm(forms.ModelForm):
    class Meta:
        model = Entidade
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'id': 'nome',
                    'required': True
                }
            ),
            'nif': forms.TextInput(
                attrs={
                    'id': 'nif',
                    'required': True
                }
            ),
        }              

class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'id': 'nome',
                    'required': True
                }
            ),
            'tipo': forms.Select(
                attrs={
                    'id': 'tipo',
                    'required': True
                }
            ),
            'id_entidade': forms.Select(
                attrs={
                    'id': 'id_entidade',
                    'required': True
                }
            ),
        }              
