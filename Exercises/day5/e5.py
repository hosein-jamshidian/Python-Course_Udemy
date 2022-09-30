# #5.0
# print("AVERAGE CALCULATOR!")
# heights=input("please insert the heights?\n").split()
#
# s=0
# n=0
# for height in heights:
#    s+=int(height)
#    n+=1
# avg=s/n
# print(f"the average of {n} number of students is : {avg}")

#ravesh 2:

# print("AVERAGE CALCULATOR!")
# heights=input("please insert the heights?\n").split()
# number_of_heights=len(heights)
# for i in range(0,number_of_heights):
#     heights[i]=int(heights[i])
# avg=round(sum(heights)/number_of_heights,2)
# print(f"the average of {number_of_heights} number of students is : {avg}")

#5.1
#
# print("HIGHEST NUMBER !")
# numbers=input("please give me you're numbers?\n").split()
# temp=0
#
# for number in numbers:
#     number =int(number)
#     if number > temp:
#         temp=number
# print(f"the highest score is :{temp}")
#
# #5.2
# #1+2+4+6+...+100
#
# s=1
# for i in range(0,101,2):
#     s+=i
# print(s)

# #5.3
# print("FIZZ BUZZ GAME !")
# for number  in range(1,100):
#     if (number % 5 ==0) and (number %3 ==0) :
#         print("fizzbuzz")
#     if number % 3 == 0:
#         print("fizz")
#     elif number %5 ==0:
#         print("buzz")
#     else :
#         print(number)

#FINAL

# import random
#
# letters='a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
# numbers='1 2 3 4 5 6 7 8 9 0'.split()
# symbols='! # $ % ^ & * + ( )'.split()
#
#
# number_of_letters=int(input("please tell me how many letter would you like in you're password?\n"))
# number_of_numbers=int(input("please tell me how many number would you like in you're password?\n"))
# number_of_symbols=int(input("please tell me how many symbol would you like in you're password?\n"))
#
# l=[]
#
#
# for i in range(0,number_of_letters):
#     l.append(letters[random.randint(0,len(letters))])
# for j in range(0,number_of_numbers):
#     l.append(numbers[random.randint(0,len(numbers))])
# for k in range(0,number_of_symbols):
#     l.append(symbols[random.randint(0,len(symbols))])
#
#
# random.shuffle(l)
# password=''.join(l)
# print(f"you're password is :{password}")

#ravesh 2:
import random

letters='a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
numbers='1 2 3 4 5 6 7 8 9 0'.split()
symbols='! # $ % ^ & * + ( )'.split()

#
# number_of_letters=int(input("please tell me how many letter would you like in you're password?\n"))
# number_of_numbers=int(input("please tell me how many number would you like in you're password?\n"))
# number_of_symbols=int(input("please tell me how many symbol would you like in you're password?\n"))
#
# l=[]
# for i in range(0,number_of_letters):
#     l.append(random.choice(letters))
# for i in range(0,number_of_numbers):
#     l.append(random.choice(numbers))
# for i in range(0,number_of_symbols):
#     l.append(random.choice(symbols))
#
# random.shuffle(l)
# password=''.join(l)
# print(f"you're password is :{password}")