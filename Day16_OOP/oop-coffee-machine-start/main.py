from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu_2 = Menu()
# resource = MenuItem()
make_coffee = CoffeeMaker()
money = MoneyMachine()


make_coffee.report()
money.report()

choice = input("What would you like? (expresso/latte/cappuccino)\n").lower()


# if choice == "espresso":