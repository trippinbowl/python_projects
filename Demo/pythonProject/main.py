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

water = 500
milk = 400
coffee = 300
money = 0


def is_resource_sufficient(order_ingredients):
    """Returns True if the order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > eval(item.lower()):
            print(f"Sorry, there is not enough {item.lower()}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        globals()[item.lower()] -= order_ingredients[item]
    global money
    money += MENU[drink_name]["cost"]


while True:
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink_choice == 'off':
        break
    elif drink_choice == 'report':
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")
    elif drink_choice in MENU:
        drink = MENU[drink_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if payment >= drink["cost"]:
                change = round(payment - drink["cost"], 2)
                print(f"Here is ${change} in change.")
                make_coffee(drink_choice, drink["ingredients"])
                print(f"Here is your {drink_choice}. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Sorry, I do not understand.")
