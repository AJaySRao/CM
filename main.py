
resources = {'Water': 300,
             'Milk': 200,
             'Coffee': 100,
             'Money': 0 }

Menu_items = {'espresso': {'Water': 50,
                           #'Milk': 0,
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

total_money = 0


def report():
    """Report of the resources in the Machine"""
    print(f"Water:{resources['Water']}ml "
          f"\nMilk:{resources['Milk']}ml "
          f"\nCoffee:{resources['Coffee']}mg "
          f"\nMoney:{resources['Money']}$")


def coin_process():
    """Process the respective value of each entered coin"""
    global total_money
    print("Please insert coins")
    for coin in coins:
        received = int(input(f"how many {coin}?:"))
        total_money += coins[coin]*received


def transaction(total_money):
    """Validates the transaction made, and returns the entered extra amount back to the user"""
    if total_money >= Menu_items[choice]['Money']:
        resources['Money'] += Menu_items[choice]['Money']
        total_money -= Menu_items[choice]['Money']
        amt = '{:.2f}'.format(total_money)
        print(f"Here's the change:{amt}$ \n")
        return True
    else:
        return False


def ingredient_check(choice):
    """Checks with resources ingredients, whether the user entered drink can be made"""
    for item in resources:
        if resources[item] >= Menu_items[choice][item]:
            if transaction(total_money):
                resources[item] -= Menu_items[choice][item]
            return True
        else:
            return False

machine = True
while machine:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        report()
    elif choice == "off":
        print("Turning off the machine")
        machine = False
    else:
        if choice in Menu_items:
            if ingredient_check(choice):
                coin_process()
                if transaction(total_money):
                    print(f"Here's your {choice}, Please enjoy!")
                    total_money = 0
                else:
                    print(f"Sorry that's not enough money \n")
            else:
                print(f"Sorry there are no enough resources!")
        else:
            print("Please only choose the available drinks ! \n")





