

# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccnino): "

action_completed = True
machine_on = True

while machine_on:
    def user_decision():
        """Let the user decise with beverage they will take"""
        question = input(
            "What would you like? (espresso/latte/cappuccino):").lower()
        return question

    user_response = user_decision()
    print(user_response)

    if user_response == "off":
        machine_on = False

# TODO: 2. Turn off the coffee machione by entering "off" to the prompt

# TODO: 3. Print report

'''
When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
'''

# TODO: 4. Check resources sufficient?

# TODO: 5. Process coins

# TODO: 6. Check transaction successful?

# TODO: 7. Make Coffee
