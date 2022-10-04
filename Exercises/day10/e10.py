# #4.1

def is_leap_year(year):
    '''test that the year that touenter as a oarameter is a leap year or not'''
    if year%4==0:
        # return("yes")
        if year%100 ==0:
            # return("no")
            if year%400==0:
                return("yes")
            else:
                return("no")
        else :
            return("yes")
    else:
        return("no")
def days_in_month(month,year):
    '''take two parameters month and year and then return the month days!'''
    common_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month>12 or month<1 :
        return "not a valid number for month".title()

    if is_leap_year(year)=="yes":
        return (leap_month_days[month-1])
    elif is_leap_year(year)=="no":
        return (common_month_days[month-1])
end=False
while not end:
    year=int(input("enter a year\n".title()))
    month=int(input("enter a month\n".title()))
    print(days_in_month(year=year,month=month))
    permission=input("continue(y/n)\n".title()).lower()
    if permission=="n":
        end=True
#FINAL(CALCULATOR)
#my answer :

print("Welcome to  my CALCULATOR!")
n1=float(input("enter the first number :\n".title()))
progress=input("enter you're operation\n+\n-\n*\n/\n".title())
n2=float(input("enter the second number :\n".title()))

def summation(num1,num2):
    return num1+num2
def substraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
def answer(num1,num2):
    if progress=="+":
        return summation(num1,num2)
    elif progress=="-":
        return substraction(num1,num2)
    elif progress=="*":
        return multiplication(num1,num2)
    elif progress=="/":
        return division(num1,num2)
    else:
        return "incorrect!".title()


ans = answer(n1, n2)
end=False
while not end :

    permission=input(f"type 'y' to continue calculation with {ans} or type 'n' to start a new calculation")

    if permission=='y':
        progress=input("enter you're operation\n+\n-\n*\n/\n".title())
        n2=float(input("enter the second number :\n".title()))
        ans=answer(num1=ans,num2=n2)
        print(ans)
    elif permission=='n':
        n1 = float(input("enter the first number :\n".title()))
        progress=input("enter you're operation\n+\n-\n*\n/\n".title())
        n2 = float(input("enter the second number :\n".title()))
        ans=answer(num1=n1,num2=n2)
        print(ans)


# FINAL(CALCULATOR)
# udemy answer :
from calculator_asci_art import logo


def summation(num1,num2):
    '''for adding two number from each other'''
    return num1+num2
def substraction(num1,num2):
    '''for substract two number from each other'''
    return num1-num2
def multiplication(num1,num2):
    '''for multiplicate two number from each other'''
    return num1*num2
def division(num1,num2):
    '''for divide two number from each other'''
    return num1/num2

operations={}

operations['+']=summation
operations["-"]=substraction
operations['*']=multiplication
operations['/']=division

def calculator():
    '''recurtion'''
    print(logo)
    n1=float(input("enter first number :\n".title()))

    end=False
    while not end:
        for symbol in operations:
            print(symbol)
        op_symbol=input("pick an operation :\n".title())
        n2=float(input("enter second number :\n".title()))

        function=operations[op_symbol]
        answer=function(n1,n2)
        print(f"{n1} {op_symbol} {n2} = {answer}")
        permission=input(f"type y to continue with {answer} or type n to startover or q for quit!(y/n/q):\n")
        if permission=='y':
            n1=answer
        elif permission=="n":
            calculator()
        elif permission == "q":
            print("good bye , i'll see you soon".title())
            end=True
calculator()


