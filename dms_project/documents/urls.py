from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet , MyDocumentView , DocumentContentView
from django.urls import path

router = DefaultRouter()
router.register(r'docs', DocumentViewSet, basename='document'),


urlpatterns = router.urls


urlpatterns += [
    path('my-docs/' , MyDocumentView.as_view() , name="my-docs"),
    path("docs/<int:pk>/content/", DocumentContentView.as_view() , name='doc-content')
    
]