from turtle import Turtle, Screen

from pointer import Pointer

screen=Screen()
screen.title('U.S state game')
screen.bgpic('blank_states_img.gif')

#TODO: make screen prepare.

pointer=Pointer()

#TODO: calling Pointer class.

while len(pointer.correct_list)<50:
    suggest = screen.textinput(title=f'{len(pointer.correct_list)}/50 States Correct',
                               prompt="What another state name:").title()
    pointer.apply_name(suggest)
    if pointer.wrong_guess_num>3:
        break

pointer.final_results()
pointer.residual_state()

#TODO: while loop that make U.S game.

screen.exitonclick()