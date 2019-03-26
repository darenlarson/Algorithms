#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # Initialize batches to infinity
    batches = float("infinity")

    # Loop over each key/value pair in recipe
    for key, value in recipe.items():

        # If the key in recipe does not exist in ingredients, you cannot make any batches
        if key not in ingredients:
            batches = 0
            return batches
        
        # Calculate the # of batches each ingredient would allow for
        ingredientsBatch = int(ingredients[key] / value)

        # The ingredient with the minimum # of batches is the maximum # of batches of the recipe that can be made
        if ingredientsBatch < batches:
            batches = ingredientsBatch

    return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
  ingredients = { 'milk': 1288, 'flour': 9, 'sugar': 95 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))