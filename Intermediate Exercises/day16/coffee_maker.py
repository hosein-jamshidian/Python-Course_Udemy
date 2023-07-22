class CoffeeMaker:
    def __init__(self):
        self.resources={
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"water:{self.resources['water']}")
        print(f"milk:{self.resources['milk']}")
        print(f"coffee:{self.resources['coffee']}")


    def is_resource_sufficient(self,drink):
        for item in drink.ingredients:
            if drink.ingredients[item]>self.resources[item]:
                print('sorry.there is not enough{item}')
                return False
        return True
    def make_coffee(self,order):
        for item in order.ingredients:
            self.resources[item]-=order.ingredients[item]
        print(f"here is you're{order.name} . enjoy!")

