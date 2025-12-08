from rest_framework import routers
from .api import ProyectViewSet,SumaViewSet,TipoViewSet,AlergiasViewSet





router = routers.DefaultRouter()

router.register('api/projects',ProyectViewSet, 'projects')
router.register('api/suma',SumaViewSet, 'suma')
router.register('api/tipo',TipoViewSet, 'tipo')
router.register('api/alergias',AlergiasViewSet, 'alergias')
urlpatterns = router.urls # me genera las urls para el crud
