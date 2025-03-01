water = 300
milk = 200
coffee = 100
money = 0

# menu
# espresso: 50ml water, 18g coffee | $1.50
# latte: 200ml water, 24g coffee, 150ml milk | $2.5
# cappuccino: 250ml water, 24g coffee, 100ml milk | $3

# Coins
# 0.01 Penny
# 0.05 nickel
# 0.10 dime
# 0.25 quar  ter

# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "

action_completed = True
machine_on = True
water = 300
milk = 200
coffee = 100
money = 0

quarter_value = 0.25
dimes_value = 0.10
nickels_value = 0.05
pennies_value = 0.01

# espresso = 50ml water, 18g coffee, $1.5
# latte = 200ml water, 24g coffee, 150ml milk, $2.50
# cappuccino = 250ml water, 24g coffee, 100ml milk, $3

def value_per_order(quarters, dimes, nickels, pennies):
    q_total = quarters * quarter_value
    d_total = dimes * dimes_value
    n_total = nickels * nickels_value
    p_total = pennies * pennies_value
    total = q_total + d_total + n_total + p_total
    return total




while machine_on:
    def user_decision():
        """Let the user decise with beverage they will take"""
        question = input(
            "What would you like? (espresso/latte/cappuccino):").lower()
        return question

    user_response = user_decision()
    # print(user_response)

# TODO: 2. Turn off the coffee machione by entering "off" to the prompt
    if user_response == "off":
        machine_on = False
<<<<<<< HEAD
    elif user_response ==  "report":
        print(f'Water: {water}ml')
        print(f'Water: {milk}ml')
        print(f'Water: {coffee}g')
        print(f'Water: ${money}')
    elif user_response == 'espresso':
        print('Plese insert coins.')
        quarters = float(input('How many quarters?: '))
        dimes = float(input('How many dimes?: '))
        nickels = float(input('How many nickels?: '))
        pennies = float(input('How many pennies?: '))

        order_amount = value_per_order(quarters=quarters, dimes=dimes, nickels=nickels, pennies=pennies)
        print(order_amount)
=======
    elif user_response == "report":
        print(f"""
        water: {water},
        milk: {milk},
        coffee: {coffee},
        Money: {money}
        """)
>>>>>>> 38b45a5325e296eb946b23944c4b490e33e0c5be


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

# TODO: 5. Proccess coins

# TODO: 6. Check transaction successful?

# TODO: 7. Make Coffee
