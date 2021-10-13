from products import MENU
from products import resources

is_on = True
money = 0
change = 0
profit = 0
def report():
    #provide the resources
    print(f'water: {resources["water"]} ml')
    print(f'milk: {resources["milk"]} ml')
    print(f'coffee: {resources["coffee"]} mg')
    print(f'money: {profit}')

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
        else:
            resources[item] = resources[item] - order_ingredients[item]
            return True


def add_money(choice):
     global money
     global change
     global profit
     money = int(input('add some money:'))
     if money > MENU[choice]['cost']:
         change = money - MENU[f'{choice}']['cost']
         print('enjoy your coffee ☕️️')
         print(f'take your change 💵{change}')
         profit = profit + MENU[choice]['cost']
     else:
         print("please add sufficient funds ❌  ")


while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino) :").lower()
    if choice == 'report':
        report()
    elif choice == 'off':
        is_on = False
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            #if resource is true i.e, sufficient it ask money
            add_money(choice)

