from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Beverage, Ingredient, BeverageIngredient
from .serializers import BeverageSerializer, IngredientSerializer

class BeverageViewSet(viewsets.ModelViewSet):
    queryset = Beverage.objects.all()
    serializer_class = BeverageSerializer

    @action(detail=True, methods=['post'])
    def dispense(self, request, pk=None):
        beverage = self.get_object()
        ingredients = BeverageIngredient.objects.filter(beverage=beverage)
        
        insufficient_ingredients = []
        for ingredient in ingredients:
            if ingredient.ingredient.quantity < ingredient.quantity:
                insufficient_ingredients.append(ingredient.ingredient.name)

        if insufficient_ingredients:
            return Response({
                'status': 'insufficient ingredients',
                'ingredients': insufficient_ingredients
            }, status=status.HTTP_400_BAD_REQUEST)

        for ingredient in ingredients:
            ingredient.ingredient.quantity -= ingredient.quantity
            ingredient.ingredient.save()

        return Response({'status': 'beverage dispensed'}, status=status.HTTP_200_OK)

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    @action(detail=True, methods=['post'])
    def update_inventory(self, request, pk=None):
        ingredient = self.get_object()
        quantity = request.data.get('quantity')
        if quantity is None:
            return Response({'status': 'invalid request'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            quantity = int(quantity)
            ingredient.quantity += quantity
            ingredient.save()
            return Response({'status': 'inventory updated'}, status=status.HTTP_200_OK)
        except (TypeError, ValueError):
            return Response({'status': 'invalid quantity'}, status=status.HTTP_400_BAD_REQUEST)
