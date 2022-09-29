# #4.0
# from Exercises.day4.help import x
#
# print("VIRTUAL COIN TOSS PROGRAM")
# if x==0:
#     print("Tail")
# elif x==1:
#     print("Head")

#4.1

import random

# names_string=input("insert tou're names with comma between :\n")
# names=names_string.split(",")
#print(type(names))
# l=len(names)
# random_number_pick=random.randint(0,l-1)
# print(f" {names[random_number_pick]} is going to buy the meal today!")

#4.2
#
# row1=['*','*','*']
# row2=['*','*','*']
# row3=['*','*','*']
# row=[row1,row2,row3]
# print(f"{row[0]}\n{row[1]}\n{row[2]}")
# position=input("Where do you want to put the treasure?\n")
# r=int(position[0])
# c=int(position[1])
# row[r-1][c-1]="X"
# print(f"{row[0]}\n{row[1]}\n{row[2]}")
#
# #FINAL
# import random
# print("ROCK , PAPER ,SCISSORS !")
# rock='''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
# paper='''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
# scissors='''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images=[rock,paper,scissors]
#
# permission=input("Let's Play Rock Paper Scissors.Are U Ready?(y/n)\n").lower().strip()
#
# if permission=='y':
#
#     random_number = random.randint(0,2)
#     ch=int(input("Alright. What Do You Choose?(type 0 for ROCK , 1 PAPER or 2 for SCISSORS.)\n"))
#
#     if (ch >2) or (ch<0):
#         print("you're choose is not valid !💔")
#         exit()
#
#     else:
#         print("Me:\n",game_images[random_number])
#         print("YOU:\n", game_images[ch])
#
#         if random_number == 0:
#             if ch ==0 :
#                 print("YOU Draw🥲")
#             elif ch == 1:
#                 print("YOU Win😻")
#             elif ch == 2:
#                 print("YOU Lose🤭")
#         elif random_number == 1:
#             if ch == 0:
#                 print("YOU Lose🤭")
#             elif ch == 1:
#                 print("YOU Draw🥲")
#             elif ch == 2:
#                 print("YOU Win😻")
#
#         elif random_number==2:
#             if ch == 0:
#                 print("YOU Win😻")
#             elif ch == 1:
#                 print("YOU Lose🤭")
#             elif ch == 2:
#                 print("YOU Draw🥲")
#
# elif permission=="n":
#     print("ok .see you soon!❤")
# else:
#     print("please enter y or n!!💔")
#     exit()
#
#
