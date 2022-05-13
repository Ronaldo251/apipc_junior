

from rest_framework import viewsets
from api.models import ArmaModel, CalibreModel, AmmoModel, ObjetoTipoModel
from api.serializers import GunSerializer, CalibreSerializer, AmmoSerializer, TypeObjectSerializer



class TypeObjectViewSet(viewsets.ModelViewSet):
    queryset = ObjetoTipoModel.objects.all()
    serializer_class = TypeObjectSerializer
class ArmaViewSet(viewsets.ModelViewSet):
    queryset = ArmaModel.objects.all().select_related('objeto' , 'calibre')
    serializer_class = GunSerializer
class AmmoViewSet(viewsets.ModelViewSet):
    queryset = AmmoModel.objects.all().select_related('objeto' , 'calibre')
    serializer_class = AmmoSerializer
class CalibreViewSet(viewsets.ModelViewSet):
    queryset = CalibreModel.objects.all()
    serializer_class = CalibreSerializer
