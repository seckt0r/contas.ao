from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User


def recibos_directoru_path(instance, filename):
    return 'usuario_{0}/{1}'.format(instance.user.id, filename)


class Transacao(models.Model):

    TIPO = (
        ('T', 'Transferência'), # Transferencia de valores entre contas com o mesmo proprietário
        ('R', 'Receita'), # Receber valores por serviços prestados ou bens vendidos
        ('D', 'Despesa'), # Pagar valores por serviços recebidos ou bens adquiridos
    )

    data = models.DateTimeField(
        verbose_name='Data',
        help_text='Data da transação',
        auto_now_add=True,
        null=True,
        blank=True
    )
    tipo = models.CharField(
        max_length=1,
        choices=TIPO,
        default='T',
        help_text='Escolha o tipo de transação',
        verbose_name='Tipo',
    )
    valor = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        null=True,
        help_text='Inserir o valor que pretende transacionar',
        verbose_name='Valor da transação'
    )
    id_categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Nome da categoria',
        verbose_name='Categoria'
    )
    id_origem = models.ForeignKey(
        'Conta',
        on_delete=models.CASCADE,
        default=0,
        related_name='conta_origem',
        help_text='Inserir a conta de origem',
        verbose_name='Conta de origem'
    )
    id_destino = models.ForeignKey(
        'Conta',
        on_delete=models.CASCADE,
        default=0,
        related_name='conta_destino',
        help_text='Inserir a conta de destino',
        verbose_name='Conta de destino'
    )

    class Meta:
        verbose_name_plural = 'Transações'

    def __str__(self):
        return 'Transação %s' % (self.id)

    def get_absolute_url(self):
        return reverse('transacoes:listar')


class Categoria (models.Model):
    nome = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        name='nome',
        help_text='Nome da categoria',
        verbose_name='Nome'
    )

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome


class Conta (models.Model):
    TIPO = (
        ('I', 'Pessoal'),
        ('L', 'Cliente'),
        ('P', 'Parceiro'),
        ('E', 'Empresa'),
        ('F', 'Fornecedor'),
    )

    nome = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        name='nome',
        help_text='Nome da conta',
        verbose_name='Nome'
    )
    tipo = models.CharField(
        max_length=1,
        choices=TIPO,
        default='I',
        help_text='Tipo de conta a ser criada',
        verbose_name='Tipo'
    )
    id_entidade = models.ForeignKey(
        'Entidade',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Entidade'
    )

    class Meta:
        verbose_name_plural = 'Contas'

    def __str__(self):
        return '%s -  %s - %s' % (self.nome, self.get_tipo_display(), self.id_entidade.nome)


class Banco(models.Model):
    pass


class Entidade(models.Model):
    nome = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        name='nome',
        help_text='Nome da entidade',
        verbose_name='Nome'
    )
    nif = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        name='nif',
        help_text='Número de Identificação Fiscal',
        verbose_name='NIF'
    )

    class Meta:
        verbose_name_plural = 'Entidades'

    def __str__(self):
        return self.nome


'''
    @property
    def xx(self):
        return self.xx_set.all()
'''
