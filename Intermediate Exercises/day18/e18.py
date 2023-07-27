import turtle
from turtle import Turtle ,Screen
import random

hosein =Turtle()
hosein.shape("turtle")
hosein.color("green")

#task 1:
#
# for i in range(4):
#     hosein.right(90)
#     hosein.forward(100)
#
# hosein.left(90)
#
# for i in range(4):
#     hosein.forward(100)
#     hosein.right(90)
# #task 2:(dashed line)
# #way1:
#
# hosein.color("red")
# for i in range(15):
#     hosein.forward(10)
#     hosein.penup()
#     hosein.forward(10)
#     hosein.pendown()
# #way2:
# for i in range(15):
#     hosein.forward(10)
#     hosein.pencolor("white")
#     hosein.forward(10)
#     hosein.pencolor("black")

#task 3

# i = 3
# color_list='red blue green black brown yellow purple pink gray'.split(' ')
# while i<10:
#     hosein.pencolor(color_list[i-3])
#     angle=360/i
#     for j in range(i):
#         hosein.forward(100)
#         hosein.right(angle)
#     i+=1

#task4:
# turtle.colormode(255)
# # color_list='red blue green black brown yellow purple pink gray'.split(' ')
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     return (r,g,b)
#
# hosein.speed(7)
# hosein.pensize(5)
# for _ in range(100):
#     hosein.pencolor(random_color())
#     choice=random.randint(1,4)
#
#     hosein.setheading(90*choice)
#     hosein.forward(20)

# #task 5:
# turtle.colormode(255)
#
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     return (r,g,b)
# hosein.speed(20)
#
# for _ in range(int(360/5)):
#     hosein.color(random_color())
#     hosein.circle(radius=100)
#     hosein.right(5)
#

#FINAL:hirst color

import colorgram
import random

turtle.colormode(255)
hosein.speed(100)
hosein.hideturtle()
colors=colorgram.extract('image.jpg',40)
colors=colors[4:]
#we don't want white and desktop color so we delete few first colors.
x=-200
y=-250

def start():
    hosein.penup()
    hosein.goto(x,y)
    #for drawing circle you don't need to pendown.
def each_row():
    for i in range(10):
        hosein.pencolor(random.choice(colors).rgb)
        hosein.dot(size=20)
        hosein.penup()
        hosein.forward(45)
        hosein.pendown()
for _ in range(10):
    start()
    each_row()
    y+=50


screen=Screen()
screen.exitonclick()