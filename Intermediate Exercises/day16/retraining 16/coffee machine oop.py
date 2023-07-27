class MenuItems:
    def __init__(self,name,water,milk,coffee,cost):
        self.name=name
        self.ingredients={
            'milk':milk,
            'water':water,
            'coffee':coffee
        }
        self.cost=cost

class Menu:
    def __init__(self):
        self.menu=[
            MenuItems('latte', 200, 150, 24, 2.5),
            MenuItems('espresso', 50, 0, 18, 1.5),
            MenuItems('cappuccino', 250, 50, 24, 3)
        ]
        self.list=[]

    def find_drink(self,order):
        for item in self.menu:
            if item.name==order:
                return item
        print('no item exist')

    def all_items(self):
        for item in self.menu:
            self.list.append(item.name)
        return('/'.join(self.list))

class CoffeeMaker:
    def __init__(self):
        self.source={
            'water':300,
            'coffee':100,
            'milk':200
        }

    def report(self):
        print('water:',self.source['water'],'\ncoffee:', self.source['coffee'],
              '\nmilk:',self.source['milk'])

    def is_resource_sufficientis(self,order):
        for item in order.ingredients:
            if order.ingredients[item] > self.source[item]:
                print('sorry.there is not enough{item}')
                return False
        return True
    def makecoffee(self,order):
        for item in order.ingredients:
            self.source[item]-=order.ingredients[item]
        print(f"here is you're {order.name} . enjoy!")

class MoneyMachine:
    def __init__(self):
        self.coin_values={
            'quarters': .25,
            'dimes': .1,
            'nickles': .05,
            'pennies': .01
        }
        self.money=0
        self.profit=0
    
    def report(self):
        print(f"you're current money is :",{self.profit})
    def make_payment(self):
        for coin in self.coin_values:
            self.money+=int(input(f"how many {coin}:"))
        return self.money
    def payment(self,cost):
        self.make_payment()
        if self.money>= cost:
            change=round(self.money-cost,2)
            self.profit+=cost
            self.money=0
            return True
        else:
            print('not enough money!')
            self.money=0
            return False


menu=Menu()
cm=CoffeeMaker()
mm=MoneyMachine()

is_on=True
while is_on:
    choice=input(f'what can I make for you?({menu.all_items()})')
    drink=menu.find_drink(choice)
    if mm.payment(drink.cost):
        if cm.is_resource_sufficientis(drink):
            cm.makecoffee(drink)

