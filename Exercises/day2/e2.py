# print("hello"[0])
# print("hello"[-1])
#
# #2.0
#
# num=input("please inset twodigits number :\n")
# print(type(num))
# print(num[0] ,"+", num[1] + " =" ,int((num)[0])+int((num)[1]))

#2.1
# print("BMI CALCULATOR!")
# height=float(input("please insert you're height(cm):\n"))
# weight=float(input("please insert you're weight(kg):\n"))
# print("youre BMI is :\n",int(weight/(height/100)**2))

# print("youre weight is {weight}".format(weight=weight))
# print(f"youre weight is {weight}")
#
# 3.1
# print("YOU'RE LIFE!")
# age=int(input("what is you're age ?\n"))
# total_day=90*365
# total_week=90*52
# total_month=90*12
# day_left=total_day-age*365
# week_left=total_week-age*52
# month_left=total_month-age*12
# print(f"if you live for 90 years so you have still {total_day} days and {total_week} weeks and {total_month} to die!!:(")

# # FINAL
#
# print("Welcome To The Tip Calculator!")
# total_bill=float(input("what is you're total bill?(Toman)\n"))
# perc=int(input("what percentage tip would you like to give?(10,12 or 15)?\n"))
# num=int(input("how many people to split the bill?"))
# temp=total_bill*((100+perc)/100)/num
# print(f"each person should pay :{round(temp,2)} Toman")

#one point:

# a="{:.2f}".format(150*((100+12)/100)/5)
# print(f"answer is {a}")

# a=150*((100+12)/100)/5
# b=12
# print(f"my answer is %.2f and my perc is %i"%(a,b))