# #16.1
#
# from prettytable import PrettyTable
# table=PrettyTable()
#
# table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column('Type', ['Electric', 'Water', 'Fire'])
# table.align='l'
# print(table)

#16.2
from menu import MenuItem,Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
o=Menu()
m=MoneyMachine()
c=CoffeeMaker()

is_on=True
while is_on:
    options=o.get_items()
    choice=input(f"what would you like?({options})")
    if choice=='off':
        is_on=False
    elif choice=='report':
        m.report()
        c.report()
    else:
        drink=o.find_item(order=choice)
        if m.make_payment(cost=drink.cost):
            if c.is_resource_sufficient(drink):
                c.make_coffee(drink)