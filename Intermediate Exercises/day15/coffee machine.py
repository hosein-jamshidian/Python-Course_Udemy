#COFFEE MACHINE :
from ART import LOGO
from requierments import menu ,coin
resource={
    'water':300,
    'milk':200,
    'coffee':100,
}
#ravesh udemy:
# def check_resources(order):
#     for item in order:
#         if order[item] >= resource[item]:
#             print("not enough")
#             return False
#     return True

#ravesh khodam:
def check_resource(order ,water_device ,milk_device ,coffee_device):
    '''this function check the primary resources and if resources is enough for order then return True
     and if not return False.'''
    if order=="espperso":
        if menu[order]["ingredients"]['water']<=water_device:
            if menu[order]["ingredients"]["coffee"]<=coffee_device:
                return True
            else:
                print("Sorry there is not enough coffee.")
                return False
        print("Sorry there is not enough water.")
        return False

    elif order=="cuppoccino":
        if menu[order]["ingredients"]['water'] <= water_device:
            if menu[order]["ingredients"]["coffee"] <= coffee_device:
                if menu[order]["ingredients"]["milk"] <= milk_device:
                    return True
                else:
                    print("Sorry there is not enough milk.")
                    return False
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False

    elif order=="latte":
        if menu[order]["ingredients"]['water'] <= water_device:
            if menu[order]["ingredients"]["coffee"] <= coffee_device:
                if menu[order]["ingredients"]["milk"] <= milk_device:
                    return True
                else:
                    print("Sorry there is not enough milk.")
                    return False
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False
# TODO :6. check sources function.

def total_coin():
    '''this function get from the user money and return the summation.'''
    print("please insert coins.".title())
    pay_list=[]
    for key in coin:
        pay_list.append(int(input(f"how many {key}:".title()))*coin[key])
    return sum(pay_list)
# TODO :7. summation all coin take from user function.

def payment(total ,cost ,money):
    '''this function is comparing the cost of the product and give the report of the situation about the user can take coffee or not
    and in the end if user take the coffee we return the money we eget from him/her.'''
    if total > cost:
        money_change = round(total - cost, 2)
        print(f"“Here is ${money_change} dollars in change.")
        print(f"Here is your {coffee_ordered}. Enjoy!")
        money +=cost
        return money

    elif total == cost:
        print(f"Here is your {coffee_ordered}. Enjoy!")
        money += cost
        return money

    else:
        print("“Sorry that's not enough money. Money refunded.")
        return False

# TODO :8. give coffee if condition was True and calculate the money we make.


def calculate_resource(order ,water ,milk ,coffee):
    '''this function after each user take them coffee's start to rebuilding the sources.'''
    if order=="espperso":
        water=water-menu[order]["ingredients"]["water"]
        coffee=coffee-menu[order]["ingredients"]["coffee"]
        print(f"water :{water}\ncoffee :{coffee}")
        return water,coffee

    elif order=="cuppoccino":
        water = water - menu[order]["ingredients"]["water"]
        coffee = coffee - menu[order]["ingredients"]["coffee"]
        milk = milk - menu[order]["ingredients"]["milk"]
        print(f"water :{water}\ncoffee :{coffee}\nmilk :{milk}")
        return water,coffee,milk

    elif order=="latte":
        water = water - menu[order]["ingredients"]["water"]
        coffee = coffee - menu[order]["ingredients"]["coffee"]
        milk = milk - menu[order]["ingredients"]["milk"]
        print(f"water :{water}\ncoffee :{coffee}\nmilk :{milk}")
        return water, coffee, milk
# TODO :9. calculate the sources after machine use the sources for give coffee to user.


water = 300
milk = 200
coffee = 100
money = 0

print(LOGO)

off=False
while not off:

    coffee_ordered = input("what would you like ?(espperso/latte/cuppoccino)\n".title()).lower()
    if coffee_ordered=="off":
        print("Have a Good Day!")
        off = True
        continue
    # TODO :1.secret key that turn off the machine.


    if coffee_ordered=='report':
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}ml\nMoney: {money}$")
        continue
    # TODO :2.secret key that report  the soureces.


    cost = menu[coffee_ordered]['cost']

    if coffee_ordered=="espperso":
        if check_resource(order=coffee_ordered,water_device=water,milk_device=milk,coffee_device=coffee):
            # cost = menu[coffee_ordered]['cost']
            total_pay = total_coin()
            money=payment(total_pay,cost,money)
            if money==False:
                continue
            water, coffee =calculate_resource(coffee_ordered,water,milk,coffee)
    # TODO :3.espperso.


    elif coffee_ordered=="cuppoccino":
        if check_resource(order =coffee_ordered,water_device =water,milk_device=milk,coffee_device =coffee):
            # cost = menu[coffee_ordered]['cost']
            total_pay = total_coin()
            money=payment(total_pay, cost,money)
            if money==False:
                continue
            water ,coffee ,milk = calculate_resource(coffee_ordered,water,milk,coffee)
    # TODO :4.cuppoccino.

    elif coffee_ordered=="latte":
        if check_resource(order=coffee_ordered,water_device=water,milk_device=milk,coffee_device=coffee):
            # cost = menu[coffee_ordered]['cost']
            total_pay = total_coin()
            money=payment(total_pay, cost,money)
            if money==False:
                continue
            water, coffee, milk = calculate_resource(coffee_ordered,water,milk,coffee)
    # TODO :5.latte.

# else:
    #drink=menu[choice]
    #if check_resource(drink["ingredients"]):