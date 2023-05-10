# Crafteds Probabilities 1.1.2
# Made by FAZuH

import Message

while True:
    try:
        Message.ingredientAmt()
        Message.probabilites()
        Message.moreOrLess()
        
    except Exception as e:
        Message.print_red(f'Error: {str(e)}')