class MenuItem:
    def __init__(self,name,water,milk,coffee,cost):
        self.name=name
        self.cost=cost
        self.ingredients={
            'milk':milk,
            'water':water,
            "coffee":coffee
        }

class Menu:
    def __init__(self):
        self.menu=[
            MenuItem('latte', 200, 150, 24, 2.5),
            MenuItem('espresso', 50, 0, 18, 1.5),
            MenuItem('cappuccino', 250, 50, 24, 3)
        ]

    def menu_type(self):
        l=[]
        for item in self.menu:
            l.append(item.name)
            l.append("/")
        return("".join(l))

    def check_exist(self,order):
        for item in self.menu:
            if item.name==order:
                return item
        print("no item exist.".title())


class CatchMoney:
    coins={
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit=0
        self.total_money=0


    def report_money(self):
        print(f"the money yo have made till now: {self.profit}".title())

    def money_calculate(self):
        print("insert you're money please.")
        for coin in self.coins:
            self.total_money+=(int(input(f"how many {coin} :"))*self.coins[coin])
        return self.total_money

    def payment(self,cost):
        self.money_calculate()
        if self.total_money>=cost:
            change=round(self.total_money-cost,2)
            print(f"here is you're chanege :{change}")
            self.profit+=cost
            self.total_money=0
            return True
        else:
            print("not enough money!")
            self.total_money = 0
            return False


class MakeCoffee:
    def __init__(self):
        self.sources ={
            'water':300,
            'milk':200,
            'coffee':100
        }
    def report_sources(self):
        print(f"water :{self.sources['water']}")
        print(f"milk :{self.sources['milk']}")
        print(f"coffee :{self.sources['coffee']}")

    def is_enough_sources(self,order):
        for item in order.ingredients:
            if self.sources[item] < order.ingredients[item]:
                print(f"we not enough {item} to make {order} for you.")
                return False
        return True

    def make_coffee(self,order):
        for item in order.ingredients:
            self.sources[item]-=order.ingredients[item]
        print(f"here is you're '{order.name}'. enjoy!")


menu=Menu()
catch_money=CatchMoney()
make_coffee=MakeCoffee()

is_on=True
while is_on:
    options=menu.menu_type()
    choice=input(f"what would you like to drink? ({options})\n").lower().strip()
    if choice=='off':
        print("Turn Off")
        is_on=False
    elif choice=="report":
        catch_money.report_money()
        make_coffee.report_sources()
    else:
        drink=menu.check_exist(choice)
        if catch_money.payment(drink.cost):
            if make_coffee.is_enough_sources(drink):
                make_coffee.make_coffee(drink)


