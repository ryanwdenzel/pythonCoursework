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

money = 0
initialRequest = "What would you like? (espresso/latte/cappuccino)"

while True:
    order = input(initialRequest)

    order = order.lower()
    if order == "off":
        break

    if order == "report":
        for i in resources:
            print("{0}: {1}ml".format(i.capitalize(), resources[i]))
        print("Money: ${}".format(money))
        continue

    resourceSuccess = True
    if order in MENU:
        for i in MENU[order]["ingredients"]:
            if resources[i] < MENU[order]["ingredients"][i]:
                print("Sorry, there is not enough {}".format(i))
                resourceSuccess = False

    if not resourceSuccess:
        continue

    if order in MENU:
        print("Price of {0} is ${1}:".format(order, MENU[order]["cost"]))
        quarters = int(input("how many quarters: "))
        dimes = int(input("how many dimes: "))
        nickles = int(input("how many nickles: "))
        pennies = int(input("how many pennies: "))
        total = (quarters * .25 + dimes * .1 + nickles * .05 + pennies * 0.01)
        print("Entered ${}.".format(total))
        if total >= MENU[order]["cost"]:
            money += MENU[order]["cost"]
            change = total - MENU[order]["cost"]
            if change > 0:
                print("Here is ${} in change.".format(round(change, 2)))

        else:
            "Sorry, that's not enough money. Money refunded."
            continue

        for i in MENU[order]["ingredients"]:
            resources[i] -= MENU[order]["ingredients"][i]
        print("Here is your {}. Enjoy!".format(order))
        initialRequest = "Wounld you like something else? (espresso/latte/cappuccino)"
    else:
        print("{} is not on the menu. Consider additional tip if you want custom orders.".format(order))
