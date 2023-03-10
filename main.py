"""---------------------------------------- Menu Definition ----------------------------------------

In this part of the code, it is determined what items the menu contains and what materials and how much are needed to
prepare each item.
"""
menu = {
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

"""---------------------------------------- Resources Definition ----------------------------------------

This part of the code specifies what resources and how much of each are available to prepare the orders.
"""

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

"""---------------------------------------- Valid Currencies Definition ----------------------------------------

In this part of the code, the valid monetary units and the value of each of them are specified.
"""

coin = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}


def check_transaction(item, cost, money, order):
    """---------------------------------------- The function to calculate the rest of the money Definition -----------------

    In this part of the code, the amount of money that should be returned to the customer is calculated.
    """
    if money < menu[item][cost]:
        return f"Sorry that's not enough money. Money refunded."
    else:
        cng = money - menu[item][cost]
        if order == "espresso":
            resources['water'] -= 50
            resources['coffee'] -= 18
        elif order == "latte":
            resources['water'] -= 200
            resources['milk'] -= 150
            resources['coffee'] -= 24
        elif order == "cappuccino":
            resources['water'] -= 250
            resources['milk'] -= 100
            resources['coffee'] -= 24
        return f"Here is ${cng} in change.\nHere is your {item} ☕️. Enjoy!"


def coffe_run():
    """---------------------------------------- Main body of code ----------------------------------------

    In this part of the code, First, the order is received. Then, according to the availability of resources, it becomes
    possible to respond to the order. Then the amount of the order is received from the user and the amount of money that
    can be returned is calculated based on the amount received and the price of the order.
    """

    # ---------------------------------------- Order Reception ----------------------------------------
    order = input("What would you like? (espresso/ latte/ cappuccino/ report):")
    # ---------------------------------------- Checking sources ----------------------------------------
    money = float(0)
    if order == "report":
        print(
            f'Water: {resources["water"]} ml\nMilk: {resources["milk"]} ml\nCoffee: {resources["coffee"]} g\n'
            f'Money: ${money}')
        coffe_run()
    elif order == "espresso":
        if resources["water"] < 50:
            print("Sorry there is not enough Water.")
        elif resources["coffee"] < 18:
            print("Sorry there is not enough Coffee.")
    elif order == "latte":
        if resources["water"] < 200:
            print("Sorry there is not enough Water.")
        elif resources["milk"] < 150:
            print("Sorry there is not enough Milk.")
        elif resources["coffee"] < 24:
            print("Sorry there is not enough Coffee.")
    elif order == "cappuccino":
        if resources["water"] < 250:
            print("Sorry there is not enough Water.")
        elif resources["milk"] < 100:
            print("Sorry there is not enough Milk.")
        elif resources["coffee"] < 24:
            print("Sorry there is not enough Coffee.")
    # ---------------------------------------- Money reception ----------------------------------------
    print("Please insert coins.")
    qtr = int(input("how many quarters?:\n"))
    dim = int(input("how many dimes?:\n"))
    ncl = int(input("how many nickles?:\n"))
    pen = int(input("how many pennies?:\n"))
    money = (qtr * coin['quarter']) + (dim * coin['dime']) + (ncl * coin['nickel']) + (pen * coin['penny'])
    # ---------------------------------------- Remaining Money Calculation ----------------------------------------
    if order == "espresso":
        print(check_transaction('espresso', 'cost', money, order))
    elif order == "latte":
        print(check_transaction('latte', 'cost', money, order))
    elif order == "cappuccino":
        print(check_transaction('cappuccino', 'cost', money, order))
    coffe_run()


# ---------------------------------------- Coffee Machine Running ----------------------------------------
coffe_run()
