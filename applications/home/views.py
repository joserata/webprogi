from rest_framework.viewsets import ModelViewSet
from .models import Definiciones, Documentos, Normatividad, Eventos
from .serializers import (
    DefinicionesSerializer,
    DocumentosSerializer,
    NormatividadSerializer,
    EventosSerializer,
)

class DefinicionesViewSet(ModelViewSet):
    queryset = Definiciones.objects.all()
    serializer_class = DefinicionesSerializer

class DocumentosViewSet(ModelViewSet):
    queryset = Documentos.objects.all()
    serializer_class = DocumentosSerializer

class NormatividadViewSet(ModelViewSet):
    queryset = Normatividad.objects.all()
    serializer_class = NormatividadSerializer

class EventosViewSet(ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
