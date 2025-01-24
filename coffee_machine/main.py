MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
resources["money"] = 0

def coffee_machine():
    u_input = input("What would you like? (espresso/latte/cappuccino):")
    if u_input == "espresso":
        if MENU['espresso']['ingredients']['water'] < resources['water'] and MENU['espresso']['ingredients']['coffee'] < resources['coffee']:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            resources["water"] -= MENU['espresso']['ingredients']['water']
            resources["coffee"] -= MENU['espresso']['ingredients']['coffee']
            resources["money"] +=  MENU['espresso']['cost']
            u_money = ((quarters * 0.25) + (nickles * 0.05) + (dimes * 0.10) + (pennies * 0.01)) - MENU['espresso']['cost']
            rounded_u_money = round(u_money,2)
            print(f"Here is {rounded_u_money} in change.")
            print("Here is your espresso. Enjoy!")
        else:
            if MENU['espresso']['ingredients']['water'] > resources['water']:
                print("Sorry there is not enough water")
            elif MENU['espresso']['ingredients']['coffee'] > resources['coffee']:
                print("Sorry there is not enough coffee")

        coffee_machine()


    elif u_input == "latte":
        if MENU['latte']['ingredients']['water'] < resources['water'] and MENU['latte']['ingredients']['coffee'] < resources['coffee'] and MENU['latte']['ingredients']['milk'] < resources['milk']:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            resources["water"] -= MENU['latte']['ingredients']['water']
            resources["coffee"] -= MENU['latte']['ingredients']['coffee']
            resources["milk"] -= MENU['latte']['ingredients']['milk']
            resources["money"] +=  MENU['latte']['cost']
            u_money = ((quarters * 0.25) + (nickles * 0.05) + (dimes * 0.10) + (pennies * 0.01)) - MENU['espresso']['cost']
            rounded_u_money = round(u_money,2)
            print(f"Here is {rounded_u_money} in change.")
            print("Here is your latte. Enjoy!")
        else:
            if MENU['latte']['ingredients']['water'] > resources['water']:
                print("Sorry there is not enough water")
            elif MENU['latte']['ingredients']['coffee'] > resources['coffee']:
                print("Sorry there is not enough coffee")
            elif MENU['latte']['ingredients']['milk'] > resources['milk']:
                print("Sorry there is not enough milk")
        coffee_machine()


    elif u_input == "cappuccino":
        if MENU['cappuccino']['ingredients']['water'] < resources['water'] and MENU['latte']['ingredients']['coffee'] < resources['coffee'] and MENU['latte']['ingredients']['milk'] < resources['milk']:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            resources["water"] -= MENU['cappuccino']['ingredients']['water']
            resources["coffee"] -= MENU['cappuccino']['ingredients']['coffee']
            resources["milk"] -= MENU['cappuccino']['ingredients']['milk']
            resources["money"] +=  MENU['cappuccino']['cost']
            u_money = ((quarters * 0.25) + (nickles * 0.05) + (dimes * 0.10) + (pennies * 0.01)) - MENU['espresso']['cost']
            rounded_u_money = round(u_money,2)
            print(f"Here is {rounded_u_money} in change.")
            print("Here is your cappuccino. Enjoy!")
        else:
            if MENU['cappuccino']['ingredients']['water'] > resources['water']:
                print("Sorry there is not enough water")
            elif MENU['cappuccino']['ingredients']['coffee'] > resources['coffee']:
                print("Sorry there is not enough coffee")
            elif MENU['cappuccino']['ingredients']['milk'] > resources['milk']:
                print("Sorry there is not enough milk")
        coffee_machine()
    elif u_input == "report":
        print(f"Water: {resources['water']} \nMilk: {resources['milk']}\nCoffee: {resources['coffee']} \nMoney: £{resources['money']}")
        coffee_machine()
    else:
        print("please type correctly!")
        coffee_machine()

coffee_machine()