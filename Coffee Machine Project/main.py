from art import logo

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(menu_ingredients, available_resources):
    """Check of there are enough resources for the selected drink."""
    for ingredient, required_amount in menu_ingredients.items():
        if available_resources.get(ingredient, 0) < required_amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    """Prompts the user to insert coins and calculate the total amount."""
    print("Please insert coins: ")
    total = 0
    total += int(input("How many €2 coins: ")) * 2
    total += int(input("How many €1 coins: ")) * 1
    total += int(input("How many €0.50 coins: ")) * 0.50
    total += int(input("How many €0.20 coins: ")) * 0.20
    total += int(input("How many €0.10 coins: ")) * 0.10
    total += int(input("How many €0.05 coins: ")) * 0.05
    return total

def process_payment(cost, total_inserted):
    """Handles payment and checks if enough money was inserted"""
    if total_inserted >= cost:
        change = round(total_inserted - cost, 2)
        print(f"Payment successful. Your change is €{change}.")
        return True #Payment successful
    else:
        print(f"Insufficient funds. You inserted €{total_inserted}, but the cost is €{cost:2f}. Refunding...")
        return False #Payment failed

def refill_resources():
    """ Refill the machine resources"""
    print("Refilling the machine...")
    additional_water = int(input("How much water would you like to add (ml)? "))
    additional_milk = int(input("How much milk would you like to add (ml)? "))
    additional_coffee = int(input("How much coffee would you like to add (g)? "))

    resources["water"] += additional_water
    resources["milk"] += additional_milk
    resources["coffee"] += additional_coffee

    print("The machine has been refilled!")
    print(f"Updated resources: Water: {resources['water']}ml, Milk: {resources['milk']}ml, Coffee: {resources['coffee']}g ")

def coffee_machine():
    # Adding profit as global
    global profit
    is_on = True

    while is_on:
        print(logo)
        choice = input("Would you like? '1' Espresso (€ 1.50), '2' Latte (€ 2.50) or '3' Cappuccino (€ 3.00)\n"
                       "Other options are: 'report', 'refill' or 'off' (turning machine off). What number do you choose?: ")

        if choice == 'refill':
            refill_resources()
            selected_drink = None
        elif choice == "report":
            print(f"water: {resources['water']}ml")
            print(f"milk: {resources['milk']}ml")
            print(f"coffee: {resources['coffee']}g")
            print(f"money: € {profit:.2f}")
            selected_drink = None
        elif choice == "1":
            selected_drink = "espresso"
        elif choice == "2":
            selected_drink = "latte"
        elif choice == "3":
            selected_drink = "cappuccino"
        else:
            choice = "off"
            print("The machine is turning off")
            selected_drink = None
            is_on = False


        if selected_drink:
            drink = menu[selected_drink]
            # print(drink)
            if check_resources(drink["ingredients"], resources):
                print(f"Insert € {drink['cost']:.2f}")
                # Get the total money inserted
                total_inserted = process_coins()
                # Process payment
                if process_payment(drink["cost"], total_inserted):
                    # Deduct resources if payment successful
                    for ingredient, required_amount in drink["ingredients"].items():
                        resources[ingredient] -= required_amount
                    # Add the drink's cost to the profit
                    profit += drink["cost"]
                    print(f"Making your {selected_drink}, Enjoy!")
                else:
                    print("Transaction canceled.")
                    selected_drink = None
            else:
                print("No, resources are not sufficient. Please, refill the machine.")
                selected_drink = None

# Start the coffee machine
coffee_machine()