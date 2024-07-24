from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Beverage(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, through='BeverageIngredient')

    def __str__(self):
        return self.name

class BeverageIngredient(models.Model):
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

