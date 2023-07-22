MILK=200
COFFEE=100
WATER=300
MONEY=0

resource={
'espresso':{'water':50, 'coffee':18,'milk':0,'price':1.5},
'latte':{'water':200, 'coffee':24,'milk':150,'price':2.5},
'cappuccino':{'water':250, 'coffee':24,'milk':100,'price':3}
}

coin_values={
'quarters':.25,
'dimes':.1,
'nickles':.05,
'pennies':.01
}

def making(order):
    if order == 'report':
        print(f"water:{WATER}ml\ncoffee:{COFFEE}g\nmilk:{MILK}ml\nmoney:{MONEY}$")
    else :
        take_money(order)

def take_money(order):
    global resource,coin_values
    if (order =='espresso') or (order =='latte') or (order =='cappuccino'):
        if check_resources(order):
            quarters = int(input('please insert coins.\nhow many quarters? '))
            dimes = int(input('how many dimes? '))
            nickles = int(input('how many nickles? '))
            pennies = int(input('how many pennies? '))

            sum_dollar=(quarters*coin_values['quarters'])+(dimes*coin_values['dimes'])+\
                       (nickles*coin_values['nickles'])+(pennies*coin_values['pennies'])

            change=round(resource[order]['price']-sum_dollar,2)

            if  change<0:
                print (f'here is {0-change}$ in change.')
                using_resource(order)
                print('bon apetite')
            elif change == 0:
                print(f'Thank you!')
                using_resource(order)
                print('*bon apetite*')
            else:
                print(f"I'm sorry but you need to pay {abs(0-change)} more money! please try again")
                take_money(order)
        else:
            print("my resources is done! please fill me up.\nPlease Use 'report' or 'exit'")
    else:
        print("I'm sorry but you're order is not in list!")

def check_resources(order):
    global MILK, COFFEE, WATER, MONEY
    if (MILK >= resource[order]['milk']) and (COFFEE >= resource[order]['coffee']) and (WATER >= resource[order]['water']):
        return True

def using_resource(order):
    global MILK,COFFEE,WATER,MONEY
    MILK= MILK-resource[order]['milk']
    COFFEE= COFFEE-resource[order]['coffee']
    WATER= WATER-resource[order]['water']
    MONEY= MONEY+resource[order]['price']


NOTEND=True

while NOTEND:
    order = input('what would you like?(espresso/latte/cappuccino):').lower()
    if order == 'exit':
        break
    making(order)

