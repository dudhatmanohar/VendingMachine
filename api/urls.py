from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BeverageViewSet, IngredientViewSet

router = DefaultRouter()
router.register(r'beverages', BeverageViewSet, basename='beverage')
router.register(r'ingredients', IngredientViewSet, basename='ingredient')

urlpatterns = [
    path('', include(router.urls)),
]
