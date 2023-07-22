class MenuItem:

    def __init__(self, name, water, milk, coffee, cost):
        self.name=name
        self.cost=cost
        self.ingredients ={
            'water':water,
            'milk':milk,
            'coffee':coffee
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]
    def get_items(self):
        l=[]
        for item in self.menu:
            l.append(item.name)
            l.append("/")
        return "".join(l)


    def find_item(self,order):
        for item in self.menu:
            if order==item.name:
                return item
        print('sorry that item is not available.')

