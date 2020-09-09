from django.contrib import admin

from transacoes.models import Transacao, Categoria, Entidade, Conta, Banco

admin.site.register(Transacao)
admin.site.register(Categoria)
admin.site.register(Entidade)
admin.site.register(Conta)
admin.site.register(Banco)
