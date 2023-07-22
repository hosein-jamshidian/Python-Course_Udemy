class MoneyMachine:
    coins={
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit=0
        self.money_recieved=0


    def report(self):
        print(f"money recieved :{self.profit}")


    def process_coins(self):
        print("pleasse insert the coins")
        for coin in self.coins:
            self.money_recieved+=int(input(f'how many {coin}?'))*self.coins[coin]
        return self.money_recieved


    def make_payment(self,cost):
        self.process_coins()
        if self.money_recieved>=cost:
            change=round(self.money_recieved-cost,2)
            print(f'here is {change} in change.')
            self.profit+=cost
            self.money_recieved
            return True
        else:
            print("sorry that's not enough money.")
            self.money_recieved=0
            return False