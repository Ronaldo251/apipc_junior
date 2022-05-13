from api.views import  ArmaViewSet, CalibreViewSet, AmmoViewSet, TypeObjectViewSet
from rest_framework.routers import DefaultRouter
from django.urls import  path


router = DefaultRouter()

router.register(r'calibres', CalibreViewSet, basename='calibres')
router.register(r'objetos-tipo', TypeObjectViewSet, basename='objeto-tipos')
router.register(r'armas', ArmaViewSet, basename='armas')
router.register(r'municoes', AmmoViewSet, basename='municoes')

urlpatterns = [

]

urlpatterns += router.urls
    


