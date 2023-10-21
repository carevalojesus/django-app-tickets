from django.contrib import admin
from .models import Ticket, Evento, Cliente, Pago

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Evento)
admin.site.register(Cliente)
admin.site.register(Pago)