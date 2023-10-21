from django.db import models


# Create your models here.
class Evento(models.Model):
    nombre_evento = models.CharField(max_length=255)
    fecha_hora = models.DateTimeField()
    lugar = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="eventos", null=True, blank=True)
    activo = models.BooleanField(default=True)

    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre_evento


class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50, null=True, blank=True)
    celular = models.CharField(max_length=9)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombres + " " + self.apellidos


class Ticket(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    codigo_unico = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.codigo_unico


class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=5, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
        ('reembolsado', 'Reembolsado'),
    ])
    cancelado = models.BooleanField(default=False)

    def __str__(self):
        return self.cliente.nombre + " " + self.cliente.apellidos + " - " + self.ticket.evento.nombre_evento + " - " + str(self.monto)
