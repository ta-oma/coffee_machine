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

profit = 0


def report_print():
    print(f"Water:{resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee:{resources['coffee']}g")
    print(f"Money:${profit}")


def is_resource_available(drink_ingredients):
    """Returns whether a drink can be made or not given ingredients and resources"""
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry there's not enough {item} !")
            return False;
    return True;


def process_coins():
    """Returns calculated coins inserted"""
    money_received = 0;
    inserted_quarter = int(input("How many quarters?"))
    inserted_dime = int(input("How many dimes?"))
    inserted_nickel = int(input("How many nickels?"))
    inserted_penny = int(input("How many pennies?"))
    money_received = (inserted_quarter * 0.25) + (inserted_dime * 0.10) + (inserted_nickel * 0.05) + \
                     (inserted_penny * 0.01)
    return money_received


def process_transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print("Here is your drink! ☕ Enjoy!")
        if change != 0:
            print(f"And here is your change of ${change}.")
    else:
        print("Sorry, not enough money!")


def process_ingredients(drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]


isMachineOn = True

while isMachineOn:
    choice = input("Please select a beverage(espresso,latte,cappuccino):")
    if choice == "report":
        report_print()
    elif choice == "off":
        print("Shutting down...")
        isMachineOn = False
    else:
        drink = MENU[choice]
        if is_resource_available(drink['ingredients']):
            process_transaction(process_coins(), drink['cost'])
            process_ingredients(drink['ingredients'])
