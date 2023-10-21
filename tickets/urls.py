from django.urls import path, include
from rest_framework import routers
from tickets import views

router = routers.DefaultRouter()
router.register('clientes', views.ClienteViewSet, 'clientes')
router.register('eventos', views.EventoViewSet, 'eventos')
router.register('pagos', views.PagoViewSet, 'pagos')
router.register('tickets', views.TicketViewSet, 'tickets')

urlpatterns = [
    path('api/', include(router.urls))
]
