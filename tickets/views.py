from rest_framework import viewsets
from .serializers import ClienteSerializer, EventoSerializer, PagoSerializer, TicketSerializer
from .models import Cliente, Evento, Pago, Ticket


# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()


class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()


class PagoViewSet(viewsets.ModelViewSet):
    serializer_class = PagoSerializer
    queryset = Pago.objects.all()


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
