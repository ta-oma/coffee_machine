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

p = 0.01
n = 0.05
d = 0.10
q = 0.25


def report_print():
    print(f"Water:{resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee:{resources['coffee']}g")
    print(f"Money:${profit}")


isMachineOn = True

while isMachineOn:
    choice = input("Please select a beverage(espresso,latte,cappuccino):")
    if choice == "espresso":
        if resources['water'] >= 50 and resources['coffee'] >= 18:
            inserted_quarter = float(input("How many quarters?"))
            inserted_dime = float(input("How many dimes?"))
            inserted_nickel = float(input("How many nickels?"))
            inserted_penny = float(input("How many pennies?"))
            total_inserted = (inserted_quarter * q) + (inserted_dime * d) + (inserted_nickel * n) + (inserted_penny * p)
            if total_inserted == 1.5:
                profit = +1.5
                resources['water'] -= 50
                resources['coffee'] -= 18
                print("Here is your espresso! ☕ Enjoy!")
            if total_inserted > 1.5:
                print("Here is your espresso! ☕ Enjoy!")
                resources['water'] -= 50
                resources['coffee'] -= 18
                change = total_inserted - 1.5
                profit += 1.5
                # TODO: Fix change decimal places
                print("And here's your change of " + str(change) + "!")
            else:
                print("Not enough money! Get outta here you bozo!")
        else:
            print("Not enough resources!")
    if choice == "report":
        report_print()
    if choice == "off":
        print("Shutting down...")
        isMachineOn = False
