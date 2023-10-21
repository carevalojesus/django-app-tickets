from django.db import transaction
from django.db.models import Sum
from rest_framework import serializers
from .models import Cliente, Ticket, Evento, Pago


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al save() original para guardar el Pago

        # Después de guardar, verifica si el Ticket relacionado está completamente pagado
        with transaction.atomic():  # abre una transacción para asegurarse de que la lógica siguiente sea atómica
            ticket = self.ticket
            total_pagado = Pago.objects.filter(ticket=ticket).aggregate(Sum('monto'))['monto__sum'] or 0

            if total_pagado >= ticket.precio:
                ticket.cancelado = True  # o cualquier campo/estado que indique que el ticket está pagado
                ticket.save()


class TicketSerializer(serializers.ModelSerializer):
    pagos = PagoSerializer(many=True, read_only=True, source='pago_set')

    class Meta:
        model = Ticket
        fields = '__all__'
