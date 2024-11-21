from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Cliente')
    numero_interno = models.CharField(max_length=20, unique=True, verbose_name='Número Interno')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')

    def __str__(self):
        return f"{self.nome} - {self.numero_interno}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    atendente = models.CharField(max_length=100, verbose_name='Nome do Atendente')
    texto_bordado = models.TextField(verbose_name='Texto a ser Bordado')
    cor_bordado = models.CharField(max_length=50, verbose_name='Cor do Bordado')
    tipo_fonte = models.CharField(max_length=50, verbose_name='Tipo de Fonte')
    data_pedido = models.DateTimeField(auto_now_add=True, verbose_name='Data do Pedido')

    def __str__(self):
        return f"Pedido de {self.cliente.nome} - {self.data_pedido.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
