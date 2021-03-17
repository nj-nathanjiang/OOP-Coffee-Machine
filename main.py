from coffee_machine import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

costs = {
    "latte": 2.5,
    "espresso": 1.5,
    "cappuccino": 3,
}

while True:
    the_order = input("What would you like? (cappuccino/latte/espresso) ").lower()
    coffee_machine = CoffeeMaker()
    cash_register = MoneyMachine
    the_menu = Menu
    found_drink = the_menu.find_drink(self=Menu(), order_name=the_order)
    if found_drink == False:
        if the_order == "report":
            coffee_machine.report()
            cash_register.report()
    else:
        if coffee_machine.is_resource_sufficient(found_drink):
            cash_register.make_payment(self=MoneyMachine(), cost=found_drink.cost)
            coffee_machine.make_coffee(found_drink)
        else:
            print("Sorry, there aren't enough resources to make your coffee.")
