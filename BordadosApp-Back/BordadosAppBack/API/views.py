from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Cliente, Pedido
from .serializers import ClienteSerializer, PedidoSerializer
from rest_framework.response import Response

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
