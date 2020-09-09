from django.urls import path, include
from .views import TransacaoList, TransacaoView, TransacaoCreate, TransacaoUpdate, TransacaoDelete, Configurar, CategoriaUpdate, CategoriaDelete, EntidadeUpdate, EntidadeDelete, ContaUpdate, ContaDelete

app_name = 'transacoes'
urlpatterns = [
    path('', TransacaoList.as_view(), name='listar'),
    path('configurar/', Configurar.as_view(), name='config'),
    path('configurar/edita_categoria/<int:pk>', CategoriaUpdate.as_view(), name='edita_categoria'),
    path('configurar/apaga_categoria/<int:pk>', CategoriaDelete.as_view(), name='apaga_categoria'),
    path('configurar/edita_entidade/<int:pk>', EntidadeUpdate.as_view(), name='edita_entidade'),
    path('configurar/apaga_entidade/<int:pk>', EntidadeDelete.as_view(), name='apaga_entidade'),
    path('configurar/edita_conta/<int:pk>', ContaUpdate.as_view(), name='edita_conta'),
    path('configurar/apaga_conta/<int:pk>', ContaDelete.as_view(), name='apaga_conta'),
]
