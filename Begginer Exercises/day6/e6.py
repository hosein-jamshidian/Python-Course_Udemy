## https://reeborg.ca/index_en.html

#Hurdle 1:

def turn_right():
    for step in range(3):
        turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6):
    jump()


# #Hurdle 2:

def turn_right():
    for step in range(3):
        turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():

    if not wall_in_front():
        move()
    else:
        jump()

# #Hurdle 3:

def turn_right():
    for step in range(3):
        turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():

    if not wall_in_front():
        move()
    else:
        jump()

#Hurdle 4:

def turn_right():
    for i in range(3):
        turn_left()


def jump():
    turn_right()
    move()
    turn_right()
    move()
    if front_is_clear():
        move()
    elif wall_in_front() == True:
        turn_left()


while at_goal() != True:
    if not wall_on_right():
        jump()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()

##ravesh 2 :

def turn_right():
    for i in range(3):
        turn_left()

def jump():
    turn_left()
    while  wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()

#storm 1 :

def turn():
    turn_left()
    move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


while not wall_in_front():
    move()
    while object_here():
        take("leaf")
turn()
while not wall_in_front():
    move()
while carries_object():
    toss("leaf")
turn_left()
move()
turn_right()
move()

##storm 2 :

def turn_right():
    for i in range(3):
        turn_left()


def eat():
    while not wall_in_front():
        move()
        while object_here():
            take("leaf")


def t_left():
    turn_left()
    move()
    turn_left()


def t_right():
    turn_right()
    move()
    turn_right()


eat()
turn_left()
eat()
t_left()
eat()
t_right()
eat()
t_left()
eat()
t_right()
eat()
t_left()
eat()
while carries_object():
    toss("leaf")
turn_left()
move()
turn_right()
move()
move()
turn_right()
move()

##Storm 3

def turn_right():
    for i in range(3):
        turn_left()


def eat_on_corner():
    while object_here():
        take("leaf")


def eat():
    while not wall_in_front():
        if front_is_clear():
            while object_here():
                take("leaf")
            move()
        elif not front_is_clear():
            while object_here():
                take("leaf")
            turn_left()
            move()
            turn_right()
            move()
            move()
            turn_right()
            move()
            turn_left()
            while object_here():
                take("leaf")


def t_left():
    turn_left()
    move()
    turn_left()


def t_right():
    turn_right()
    move()
    turn_right()


def go_home():
    turn_left()
    move()
    turn_right()
    move()
    move()
    turn_right()
    move()


eat()
eat_on_corner()
turn_left()
eat()
eat_on_corner()
t_left()

while not wall_on_right():
    eat()
    eat_on_corner()
    t_right()
    eat()
    eat_on_corner()
    t_left()

eat()

while carries_object():
    toss("leaf")
go_home()

## FINAL:

print("MAZE!")
def turn_right():
    for i in range(3):
        turn_left()


while not at_goal():

    if wall_on_right():
        while wall_in_front():
            turn_left()
        move()
    else:
        turn_right()
        while wall_in_front():
            turn_left()
        move()

##ravesh2:

print("MAZE!")
def turn_right():
    for i in range(3):
        turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()