

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resorces[item]:
            print (f"Sorry, there's not enough {item}.")
            return False
        return True

def make_coffee(order_ingredients, order):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {order} ☕. Enjoy!")
    print_report()

def process_payment(cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if total >= cost:
        remainder = total - cost
        global  profit
        profit+= cost
        print (f"Here is £{remainder:.2f} in change.")
        return True
    return False

def print_report():
    global profit
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: £{profit:.2f}")





machine_on = True

while machine_on:
    instruction = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if instruction == "off":
        machine_on = False
    elif instruction == "report":
        print_report()
    else:
        drink = MENU.get(instruction)
        can_make = check_resources(drink["ingredients"])
        if can_make:
            payment_successful = process_payment(drink["cost"])
            if payment_successful:
                make_coffee(drink["ingredients"], instruction)
            else:
                print("Sorry, that's not enough money. Money refunded.")


