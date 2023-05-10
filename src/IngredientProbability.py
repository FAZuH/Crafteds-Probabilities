from itertools import product
from numpy import prod

import IngredientIdentification as IngID

# Does math probabilities thing
def calculate():
    global ingredient_probabilities
    ingredient_probabilities = {}

    # Creates a generator expression of all possible roll permutations
    ingredient_possibleRolls = product(*IngID.ingredient_rolls_list)
    # Creates a generator expression of all possible probability permutations
    ingredient_possibleProbs = product(*IngID.ingredient_probDist_list)

    for possibleRoll, possibleProb in zip(ingredient_possibleRolls, ingredient_possibleProbs):
        # Adds probabilities to ingredient_probabilities using possible identification values as keys
        IDValue = sum(possibleRoll)
        if IDValue in ingredient_probabilities:
            ingredient_probabilities[IDValue] += prod(possibleProb)
        else:
            ingredient_probabilities[IDValue] = prod(possibleProb)