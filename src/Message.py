from colorama import Fore, Style
from decimal import Decimal

import IngredientProbability as IngProb
import IngredientIdentification as IngID

def print_red(message):
    print(Fore.LIGHTRED_EX + message + Style.RESET_ALL)

def print_green(message):
    print(Fore.LIGHTGREEN_EX + message + Style.RESET_ALL)

def print_blue(message):
    print(Fore.LIGHTBLUE_EX + message + Style.RESET_ALL)

def ingredientAmt():
    global ingredient_amount
    print_blue(f"\n - Enter the number of ingredients, type 'exit' to exit:")
    ingredient_amount = input()
    if ingredient_amount.lower() == 'exit':
        exit()
    else:
        ingredient_amount = int(ingredient_amount)
    IngID.stats()

# RESULTS
def probabilites():
    IngProb.calculate()
    print_blue(f"\nProbabilities: ")
    for IDValue, probability in IngProb.ingredient_probabilities.items():
        one_in_n = round(Decimal(1/probability), 2)
        result = f"Roll: {int(IDValue)}, Probability: {probability*100:.2f}% (1 in {one_in_n})"
        print_green(result)

def moreOrLess():
    while True:
        print_blue("\n - Enter 'more' or 'less' to check for chance of getting >= or <= than a specific value, type 'back' to go back:")
        user_input = input().lower()
        if user_input not in ['more', 'less', 'back']:
            print_red('invalid input')
            continue
        elif user_input == 'back':
            break

        print_blue("\n - Enter the value: ")
        sum_roll = int(input())
        if user_input == 'more':
            probability = sum(IngProb.ingredient_probabilities[rollValue] for rollValue in IngProb.ingredient_probabilities if rollValue >= sum_roll)
            operator = ">="
        elif user_input == 'less':
            probability = sum(IngProb.ingredient_probabilities[rollValue] for rollValue in IngProb.ingredient_probabilities if rollValue <= sum_roll)
            operator = "<="
        print_green(f"Chance of getting roll {operator}{sum_roll}: {probability*100:.2f}%")