# #3.0
# #ODD OR EVEN:
# x=int(input("please enter a integer number:\n"))
# if x%2==0:
#     print(f"{x} is an EVEN number ")
# else :
#     print(f"{x} is and ODD number ")

##program in course :

# h=float(input("give me ur height:\n"))
# if h>=120 :
#     a=float(input("give me ur age:\n"))
#     if a<=12:
#         print("you can use rollercoaster for 5$")
#     elif a<=18 :
#         print("you can use rollercoaster for 7$")
#     else :
#         print("you should pay 10$ to use rollercoaster ")
# else :
#     print("u need to wait grew up!")
#
# #3.1
#
# print("BMI CALCULATOR!")
# height=float(input("please give me you're height(cm):\n"))
# weight=float(input("please give me you're weight(kg):\n"))
# bmi=round(weight/(height/100)**2,1)
# if height>0 and weight>0:
#     if bmi <18.5:
#         print(f"you're BMI is :{bmi} , and you are UNDERWEIGHT")
#     elif bmi<25:
#         print(f"you're BMI is :{bmi} , and you are NORMAL WEIGHT")
#     elif bmi<30:
#         print(f"you're BMI is :{bmi} , and you are OVERWEIGHT")
#     elif bmi<35:
#         print(f"you're BMI is :{bmi} , and you are obese")
#     else:
#         print(f"you're BMI is :{bmi} , and you are CLINICALLY OBESE!")

# #3.2
#
# print("LEAP YEAR! ")
# year=int(input("give me you're partiular year?\n"))
# if year%4==0:
#     #print(f"till {year} is a Leap year !")
#     if year%100 ==0:
#         #print("till Not a Leap year . wait for one thing checking!")
#         if year%400==0:
#             print(f"OH the {year} is a Leap year !")
#         else:
#             print("Not a Leap year.done")
#     else :
#         print(f"{year} is a Leap year ! ")
# else:
#     print(f"{year} Not a Leap year. it has not remaider eqaual 0 !")

# #3.4
#
# print("PIZZA DELIVERIES!")
# size=input("what size pizza do you want?(s for small , m for medium and l for large) ").lower()
# add_p=input("do you want pepperoni?(y for yes and n for no) ").lower()
# extra_cheese=input("do you want extra cheese?(y for yes and n for no) ").lower()
# prise=0
#
# if size =='s':
#     prise=15
# elif size =='m':
#     prise=20
# elif size =='l':
#     prise=25
# else :
#     breakpoint()
#
# if add_p=='y' and size =='s':
#     prise+=2
#
# if add_p=='y' and size !='s':
#     prise+=3
#
# if extra_cheese=='y':
#     prise+=1
#
# print(f"you order a pizza with {size} size.you're prise is : ${prise} ")

#3.5:
#
# print("LOVE COLCULATOR!!")
# name1=input("please give me you're name :\n").lower()
# name2=input("please give me her/his name who you love it:\n").lower()
# #*we better to concate two names with themselvse and then colculate the count of each letter*
# t=name1.count("t")+name2.count("t")
# r=name1.count("r")+name2.count("r")
# u=name1.count("u")+name2.count("u")
# e=name1.count("e")+name2.count("e")
# true=t+r+u+e
# l=name1.count("l")+name2.count("l")
# o=name1.count("o")+name2.count("o")
# v=name1.count("v")+name2.count("v")
# e=name1.count("e")+name2.count("e")
# love=l+o+v+e
# love_score=int(str(true)+str(love))
#
# if love_score <10 or love_score>90 :
#     print(f"you're score is {love_score}% . you go together like coke and mentos! ;)")
# elif love_score>40 and love_score<50 :
#     print(f"you're score is {love_score} , you are alright togrther !")
# else :
#     print(f"you're score is {love_score}")

#FINAL:
#
# print("     Welcome To Treasure Island\nyou're mission is to find the treasure!\n     so if you ready lets go!")
# step1=input('Round1: you want to go "left" or "right"?\n').lower().strip()
# if step1=="right":
#     print("Game Over in round 1!")
# elif step1=="left":
#     step2=input('Rount2:OK. now you want to "wait" or "swim" ?\n').lower().strip()
#     if step2=="swim":
#         print("Game Over in round 2!")
#     elif step2=="wait":
#         step3=input("Round3: ALRIGHT which door do you pick?(red or yellow or blue)\n").lower().strip()
#         if (step3=="red") or (step3=="blue"):
#             print("Game Over in reound 3!")
#         elif step3=="yellow":
#             print("OH Wow You Win .You Found The Treasure!")
#         else:
#             breakpoint()
#     else:
#         breakpoint()
# else:
#     breakpoint()

#My Game:
#
# print("Alright. I Have Challenge For You!\nI Need You To Help Me Find My House.")
# permission=input("Would You Help Me?(y for Yes and n for No)\n").lower().strip()
# if permission =="y":
#     step1=input("Ok. I just I don't remember which city I am living . what is you're suggestion?\n").lower().strip()
#     if step1=="shiraz":
#         step2=input("Ok. I think we find my city.now let's find my street.\nI remember that I going for playing soccerball in 'Azadi' street.\nand riding a bicycle in 'Eram' garden street.\nand swimming in a pool that build in 'Chamran' street.\nwhich street you think am I living?(hint:think about my favorite sport!)\n").lower().strip()
#         if step2=="chamran":
#             step3=input("OH Well Well Well . I can see you know me well.\nI can't remember the number of  my alley.\nbut I guess the correct number between '20' or '30 or '18' or '22'.\nwhich one do you pick ?\n").lower().strip()
#             if step3=="20":
#                 step4=input("ok I'm surrender .I give you a hint and my house plaque is 276.\nBUT WAIT ! give me the last answer.\nwe have 3 room in my house.\nthe number '1' is just right bihind the entrance door.\nthe next door is door number '2' and set in the middle of the house.\nthe last door is number '3' and set in the ending of the house and it has a balcony!\nso with this information which number do you pick ?\n").lower().strip()
#                 if step4=="1":
#                     print("OH SHIT.YOU FIND ME! YOU WIN MY GAME ;)")
#                 elif (step4=="2") or (step4=="3"):
#                     print("I'm so sorry for this .but you Lose in this round.you don't pick the correct number !")
#                 else:
#                     exit()
#             elif (step3=="30") or (step3=='18') or (step3=='22'):
#                 print("No No I'm sorry .this nuber is not the right number !")
#             else:
#                 exit()
#         elif step2=="azadi" or step2=="eram":
#             print("I'm sorry but till you don't know me well you can't pass this step!")
#         else:
#             exit()
#     else:
#         print("oh no. i don't even remember a single memory of this city .let's try one more time! ")
# elif permission=="n":
#     print("Oh I'm Sad But It's Alright!")
# else:
#     exit()