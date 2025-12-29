from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet

router = DefaultRouter()
router.register(r'docs', DocumentViewSet, basename='document')

urlpatterns = router.urls
