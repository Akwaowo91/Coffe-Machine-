from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
# money_machine.report()

coffee_maker = CoffeeMaker()
# coffee_maker.report()

menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    order = input(f"What drink would you like? ({options}):")
    if order == 'off':
        is_on = False
    elif order == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                # print(payment)
                # print(resource_sufficient)
