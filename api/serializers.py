from rest_framework import serializers
from .models import Beverage, Ingredient, BeverageIngredient

class BeverageIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeverageIngredient
        fields = ['ingredient', 'quantity']

class BeverageSerializer(serializers.ModelSerializer):
    ingredients = BeverageIngredientSerializer(many=True, source='beverageingredient_set')

    class Meta:
        model = Beverage
        fields = ['name', 'ingredients']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id','name', 'quantity']
