# #8.1
# import numpy as np
# end_app=False
# while not end_app:
#     h=float(input("height of wall:(meter)\n"))
#     w=float(input("width of wall:(meter)\n"))
#     coverage=5
#     def paint_cal(heigth=h,width=w,cover=coverage):
#         value=round((width*heigth)/cover)
#         print(f"you'll needd {value} cans to pain!")
#
#     paint_cal()
#     per=input("do want to try again?(y/n)\n")
#     if per == "n":
#         end_app=True
#

# #8.2
# # my solution
# import math
# print(math.ceil(1.8))

# print("PRIME NUMBER !")
# number=int(input("give me you're integer number :\n"))
# if number <=0:
#     print("you're number isn't integer.please try again!")
# elif number ==1:
#     print("it's not a prima number!")
# else:
#     def prime_number(num=number):
#         s=0
#         for i in range(1,num+1):
#             if num%i==0:
#                 s+=1
#         if s>2:
#             print("it's not a prime number!")
#         else:
#             print("it's a prime number!")
#     prime_number()
# # 8.3
#my answer :
# while True:
#     permission=input("if you want to incode type y \nand if you want to decode type n \nand if type anything else you quit! :\n").lower().strip()
#     if permission !="n" and permission!="y":
#         exit()
#
#     alphabet = "a b c d e f g h i j k l m n o p q r s t u v w y z a b c d e f g h i j k l m n o p q r s t u v w y z".split()
#     message = input("enter you're message :\n").lower().strip()
#     shift = int(input("number of shift :\n"))
#
#     def incode(message=message, shift=shift):
#         index_list = []
#         for letter in message:
#             index_list.append(alphabet[alphabet.index(letter) + shift])
#         print(f'the incoded message is :{"".join(index_list)}\n')
#     def decode(message=message,shift=shift):
#         index_list=[]
#         for letter in message:
#             index_list.append(alphabet[alphabet.index(letter)-shift])
#         print(f'the decoded message is :{"".join(index_list)}\n')
#
#     if permission=="y":
#         incode()
#     elif permission=='n':
#         decode()

#course answer:(complete answer)
from caesar_sipher_art import logo
print(logo)
end=False
while not end:

    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    permission = input("if you want to incode type incode :\nif you want to decode type decode :\n").lower().strip()
    message = input("enter you're message :\n").lower().strip()
    shift = int(input("number of shift :\n"))

    ##if the shift number bigger than 50 :
    if shift>52 :
        shift=shift%26

    def caesar(message=message,shift=shift,direction=permission):
        text_list=[]

        if direction == "decode":
            shift *= -1

        for letter in message:
            if letter in alphabet:
                ind = alphabet.index(letter)
                text_list.append(alphabet[ind + shift])
            else:
                text_list.append(letter)
        print("".join(text_list))

    caesar()

    per_end=input("do you want to continue?(y/n)")

    if per_end=="n":
        end=True
    elif per_end !="y":
        print("please enter y or n. I take it as a yes!")
print("goodbye!")


