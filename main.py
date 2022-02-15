resources = {'Water': 300,
             'Milk': 200,
             'Coffee': 100}
Menu_items = {'espresso': {'Water': 50,
                           'Milk': 0,
                           'Coffee': 18,
                           'Money': 3.5},
              'latte': {'Water': 200,
                        'Milk': 150,
                        'Coffee': 24,
                        'Money': 2.5},
              'cappuccino': {'Water': 250,
                             'Milk': 100,
                             'Coffee': 24,
                             'Money': 2.41}}
coins = {'pennies': 0.01,
         'nickels': 0.05,
         'dimes': 0.10,
         'quarters': 0.25}
profit = 0


def report():
    """Report of the resources in the Machine"""
    print(f"Water:{resources['Water']}ml "
          f"\nMilk:{resources['Milk']}ml "
          f"\nCoffee:{resources['Coffee']}mg "
          f"\nMoney:${profit}")


def coin_process():
    """Process the respective value of each entered coin"""
    print("Please insert coins")
    total_money = 0
    for coin in coins:
        received = int(input(f"how many {coin}?:"))
        total_money += coins[coin]*received
    return total_money


def transaction(cost):
    """Validates the transaction"""
    received = coin_process()
    if received >= cost:
        received -= cost
        print(f"Here's the change:{round(received, 2)}$")
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded!")
        return False


def ingredient_check(choice):
    """Checks with resources ingredients, whether the user entered drink can be made"""
    for item in resources:
        if resources[item] >= Menu_items[choice][item]:
            return True
        else:
            print(f"Sorry there are no enough available {item}!")
            return False


def make_coffee():
    for item in resources:
        if resources[item] >= Menu_items[choice][item]:
            resources[item] -= Menu_items[choice][item]
    print(f"Here's your {choice}, Please enjoy!")

machine = True
while machine:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        report()
    elif choice == "off":
        print("Turning off the machine")
        machine = False
    else:
        if choice in Menu_items:
            if ingredient_check(choice):
                cost = Menu_items[choice]['Money']
                if transaction(cost):
                    make_coffee()
                    profit += cost
        else:
            print("Please only choose the available drinks ! \n")





