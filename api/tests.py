from django.test import TestCase
from rest_framework.test import APIClient
from .models import Beverage, Ingredient, BeverageIngredient

class VendingMachineTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        water = Ingredient.objects.create(name='water', quantity=10)
        coffee = Ingredient.objects.create(name='coffee', quantity=10)
        milk = Ingredient.objects.create(name='milk', quantity=10)
        sugar = Ingredient.objects.create(name='sugar', quantity=10)

        black_coffee = Beverage.objects.create(name='Black Coffee')
        BeverageIngredient.objects.create(beverage=black_coffee, ingredient=water, quantity=3)
        BeverageIngredient.objects.create(beverage=black_coffee, ingredient=coffee, quantity=1)
        BeverageIngredient.objects.create(beverage=black_coffee, ingredient=sugar, quantity=1)

        coffee_with_milk = Beverage.objects.create(name='Coffee with Milk')
        BeverageIngredient.objects.create(beverage=coffee_with_milk, ingredient=water, quantity=1)
        BeverageIngredient.objects.create(beverage=coffee_with_milk, ingredient=coffee, quantity=1)
        BeverageIngredient.objects.create(beverage=coffee_with_milk, ingredient=milk, quantity=2)
        BeverageIngredient.objects.create(beverage=coffee_with_milk, ingredient=sugar, quantity=1)

    def test_dispense_black_coffee(self):
        response = self.client.post('/api/beverages/1/dispense/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'beverage dispensed')

    def test_dispense_black_coffee_insufficient_ingredients(self):
        Ingredient.objects.filter(name='water').update(quantity=0)
        response = self.client.post('/api/beverages/1/dispense/')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['status'], 'insufficient ingredients')

