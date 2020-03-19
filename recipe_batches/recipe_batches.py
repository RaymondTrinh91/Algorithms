#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  amount_possible = float("inf")

  if len(recipe) > len(ingredients):
    amount_possible = 0
    return amount_possible

  for (key,value), (key2,value2) in zip(recipe.items(), ingredients.items()):
    if value > value2:
      amount_possible = 0
      return amount_possible
    elif amount_possible > value2 // value:
      amount_possible = value2 // value
  
  return amount_possible

recipe_batches({ 'milk': 100, 'butter': 50, 'flour': 5 },{ 'milk': 132, 'butter': 48, 'flour': 51 })

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))