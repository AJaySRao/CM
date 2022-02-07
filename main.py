
resources = {'Water': 300,
             'Milk': 200,
             'Coffee': 100,
             'Money': 0 }

Menu_items = {'espresso': {'Water': 50,
                           'Milk': 0,
                           'Coffee': 18,
                           'Money': 3.5},
              'latte': {'Water': 200,
                        'Milk': 150,
                        'Coffee': 24,
                        'Money': 2.5},
              'Cappuccino': {'Water': 250,
                             'Milk': 100,
                             'Coffee': 24,
                             'Money': 2.41}}

coins = {'pennies': 0.01,
         'nickels': 0.05,
         'dimes': 0.10,
         'quarters': 0.25}

total_money = 0


def report():

    print(f"Water:{resources['Water']}ml "
          f"\nMilk:{resources['Milk']}ml "
          f"\nCoffee:{resources['Coffee']}mg "
          f"\nMoney:{resources['Money']}$")


def transaction(total_money):
    if total_money >= Menu_items[choice]['Money']:
        resources['Money'] = Menu_items[choice]['Money']
        total_money -= Menu_items[choice]['Money']
        amt = '{:.2f}'.format(total_money)
        print(f"Here's the change:{amt}$")
    else:
        print(f"Sorry that's not enough money")

#
def preparation(choice):
    for item in choice[items]:
        if Menu_items[choice][item] <= resources[item]:
            resources[item] -= Menu_items[choice][item]
            print(f"Here's your:{choice}, Please enjoy!")
        else:
            print(f"Sorry there are no enough resources!")


choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

if choice == "report":
    report()
elif choice == "off":
    print("Turning off the machine")
else:
    if choice in Menu_items:
        print("Please insert coins")

        for coin in coins:
            received = int(input(f"how many {coin}?:"))
            total_money += coins[coin]*received

        preparation(choice)
        transaction(total_money)





