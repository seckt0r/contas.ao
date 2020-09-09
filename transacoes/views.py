from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .models import Transacao, Conta, Entidade, Categoria
from .forms import TransacaoForm, CategoriaForm, EntidadeForm, ContaForm


class TransacaoList(View):
    model = Transacao
    template_name = ("transacoes/transacao_list.html")

    def get(self, request, *args, **kwargs):
        transacao_list = Transacao.objects.all().order_by('-data')
        paginator = Paginator(transacao_list, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'transacao': transacao_list,
            'transacao_form': TransacaoForm,
            'page_obj': page_obj,
        }

        return render(request, "transacoes/transacao_list.html", context)

    def post(self, request, *args, **kwargs):
        transacao_form = TransacaoForm(
            request.POST or None, request.FILES or None)
        if transacao_form.is_valid():
            transacao = Transacao(
                tipo=transacao_form.cleaned_data['tipo'],
                valor=transacao_form.cleaned_data['valor'],
                id_categoria=transacao_form.cleaned_data['id_categoria'],
                id_origem=transacao_form.cleaned_data['id_origem'],
                id_destino=transacao_form.cleaned_data['id_destino'],
            )
            print("Transação Registada")
            print(transacao_form.cleaned_data)
            transacao.save()
            messages.success(request, "Nova transação registada")
            return redirect('transacoes:listar')
        else:
            print("Registo de transação falhou!")
            print(transacao_form.cleaned_data)
            messages.error(request, "Erro ao registar a transação")
            return redirect('transacoes:listar')


class Configurar(View):

    def get(self, request, *args, **kwargs):
        contas = Conta.objects.all()
        entidades = Entidade.objects.all()
        categorias = Categoria.objects.all()

        context = {
            'contas': contas,
            'conta_form': ContaForm,
            'entidades': entidades,
            'entidade_form': EntidadeForm,
            'categorias': categorias,
            'categoria_form': CategoriaForm,
        }

        return render(request, "transacoes/configurar.html", context)

    def post(self, request, *args, **kwargs):
        if 'nova_categoria' in request.POST:

            categoria_form = CategoriaForm(
                request.POST or None)
            if categoria_form.is_valid():
                c = Categoria(
                    nome=categoria_form.cleaned_data['nome'],
                )
                print("Categoria Registada")
                print(categoria_form.cleaned_data)
                c.save()
                messages.success(request, "Nova categoria registada")
                return redirect('transacoes:config')
            else:
                print("Registo de categoria falhou!")
                print(categoria_form.cleaned_data)
                messages.error(request, "Erro ao registar a categoria")
                return redirect('transacoes:config')

        if 'nova_entidade' in request.POST:
            entidade_form = EntidadeForm(
                request.POST or None)
            if entidade_form.is_valid():
                e = Entidade(
                    nome=entidade_form.cleaned_data['nome'],
                    nif=entidade_form.cleaned_data['nif'],
                )
                print("Entidade Registada")
                print(entidade_form.cleaned_data)
                e.save()
                messages.success(request, "Nova entidade registada")
                return redirect('transacoes:config')
            else:
                print("Registo de entidade falhou!")
                print(entidade_form.cleaned_data)
                messages.error(request, "Erro ao registar a entidade")
                return redirect('transacoes:config')

        if 'nova_conta' in request.POST:
            conta_form = ContaForm(
                request.POST or None)
            if conta_form.is_valid():
                c = Conta(
                    nome=conta_form.cleaned_data['nome'],
                    tipo=conta_form.cleaned_data['tipo'],
                    id_entidade=conta_form.cleaned_data['id_entidade'],
                )
                print("Conta Registada")
                print(conta_form.cleaned_data)
                c.save()
                messages.success(request, "Nova conta registada")
                return redirect('transacoes:config')
            else:
                print("Registo de conta falhou!")
                print(conta_form.cleaned_data)
                messages.error(request, "Erro ao registar a conta")
                return redirect('transacoes:config')

class CategoriaUpdate(View):
    pass

class EntidadeUpdate(View):
    pass

class ContaUpdate(View):
    pass

class CategoriaDelete(View):
    def get(self, request, pk, *args, **kwargs):
        Categoria.objects.get(id=pk).delete()
        return redirect('transacoes:config')

class EntidadeDelete(View):
    def get(self, request, pk, *args, **kwargs):
        Entidade.objects.get(id=pk).delete()
        return redirect('transacoes:config')

class ContaDelete(View):
    def get(self, request, pk, *args, **kwargs):
        Conta.objects.get(id=pk).delete()
        return redirect('transacoes:config')

class TransacaoView(DetailView):
    model = Transacao


class TransacaoCreate(CreateView):
    model = Transacao
    form_class = TransacaoForm
    success_url = reverse_lazy('transacao:listar')


class TransacaoUpdate(UpdateView):
    model = Transacao
    form_class = TransacaoForm
    success_url = reverse_lazy('transacao:listar')


class TransacaoDelete(DeleteView):
    model = Transacao
    success_url = reverse_lazy('transacao:listar')
