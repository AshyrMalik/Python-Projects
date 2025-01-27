from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# print(menu.get_items())
# print(menu.find_drink(input()))
#
# #
# #

while (True):
    choice = input(f"What will you like to buy: ({menu.get_items()}) ")

    if choice=="off":
        break
    elif choice=="report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink= menu.find_drink(choice)
        can_make = coffee_maker.is_resource_sufficient(drink)
        if can_make:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(choice)

