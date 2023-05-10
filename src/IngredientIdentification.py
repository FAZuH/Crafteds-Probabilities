from decimal import Decimal
from math import floor

import Message as Msg

def stats():
    global ingredient_rolls_list, ingredient_probDist_list
    ingredient_rolls_list = []
    ingredient_probDist_list = []
    ingredient_base_integers = range(101)

    Msg.print_blue("\n - Enter the min, max and effectiveness(optional) of the ID separated by a comma")
    for i in range(1, Msg.ingredient_amount+1):
        while True:
            try:
                # Basic identification info
                ingredient_input = input(f"Ingredient {i}: ").split(',')
                ingredient_stat_min = int(ingredient_input[0])
                ingredient_stat_max = int(ingredient_input[1])
                if len(ingredient_input) == 3:
                    ingredient_stat_eff = Decimal(int(ingredient_input[2])/100)
                else:
                    ingredient_stat_eff = Decimal(0)

                # Check that min <= max
                if ingredient_stat_min > ingredient_stat_max:
                    raise ValueError(Msg.print_red("Minimum value is greater than maximum value"))
                ingredient_stat_range = abs(ingredient_stat_max - ingredient_stat_min)

                # Check that eff is between 0 and 1
                if ingredient_stat_eff < 0 or ingredient_stat_eff > 1:
                    raise ValueError(Msg.print_red("Effectiveness must be between 0 and 100"))

                # Calculation for possible rolls
                ingredient_base_diff = Decimal(ingredient_stat_range/100)
                ingredient_base_values = [ingredient_stat_min + (ingredient_base_diff * Decimal(base_integer)) for base_integer in ingredient_base_integers]
                ingredient_base_values_rounded = [round(baseValue) for baseValue in ingredient_base_values]
                # Unique values of ingredient_baseValues_rounded
                ingredient_rolls = list(set(ingredient_base_values_rounded)) 
                # Applies ingredient effectiveness to each roll
                ingredient_rolls_boosted = [floor(roll*(ingredient_stat_eff+1)) for roll in ingredient_rolls] 
                ingredient_rolls_list.append(ingredient_rolls_boosted)

                # Calculation for probability distribution of possible rolls
                ingredient_rolls_count = [ingredient_base_values_rounded.count(roll) for roll in ingredient_rolls]
                ingredient_probDist = [Decimal(rolls_count/101) for rolls_count in ingredient_rolls_count]
                ingredient_probDist_list.append(ingredient_probDist)
                
                break  # Exit while loop on successful input

            except Exception:
                Msg.print_red(f"example: 1,2,66 for ingredient with min 1, max 2, effectiveness 66")
