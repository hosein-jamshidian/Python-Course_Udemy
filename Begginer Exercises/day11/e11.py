#BLACK JACK PROJECT!

import random
from blackjack_art import logo

cards=[
        {'A':1},
        {'2': 2},
        {'3': 3},
        {'4': 4},
        {'5': 5},
        {'6': 6},
        {'7': 7},
        {'8': 8},
        {'9': 9},
        {'10': 10},
        {"jack": 10},
        {"queen": 10},
        {'king': 10}
    ]

enter_permission=input("do you want to play a blackjack?".title()+"(y/n)\n")
if enter_permission=='n':
    print("ok goodbye".title())
    exit()
else:
    print(logo)

    # end_game=False
    # while not end_game:
    def blackjack():
        '''Recursion '''
        youre_choice=[]
        computer_choice=[]

        for i in range(2):
            youre_choice.append(random.choice(cards))
            computer_choice.append(random.choice(cards))

        youre_cards=[]
        computer_cards=[]
        youre_cards_key=[]
        computer_cards_key=[]

        for item in youre_choice:
            for key in item:
                youre_cards_key.append(key)
                youre_cards.append(item[key])

        for item in computer_choice:
            for key in item:
                computer_cards_key.append(key)
                computer_cards.append(item[key])



        print(f"you're cards: [{youre_cards_key[0]},{youre_cards_key[1]}]")
        print(f"computer first card :[{computer_cards_key[0]}]")
        bonus_card=input("do you want another card?".title()+"(y/n)\n")


        def calculate_no_bonus_card(youre_cards=youre_cards, computer_cards=computer_cards):
            '''
            return that the result for no choosing the third card!
            '''
            sum_youre_cards = sum(youre_cards)
            sum_comuter_cards = sum(computer_cards)
            if sum_youre_cards > sum_comuter_cards:
                return(f"{youre_cards_key[0]}+{youre_cards_key[1]}={sum_youre_cards} Bagger Than {computer_cards_key[0]}+{computer_cards_key[1]}={sum_comuter_cards} . So You WIN!😍")
            elif sum_youre_cards == sum_comuter_cards :
                return(f"{youre_cards_key[0]}+{youre_cards_key[1]}={sum_youre_cards} Equal To {computer_cards_key[0]}+{computer_cards_key[1]}={sum_comuter_cards} . DRAW!😐")
            else:
                return(f"{youre_cards_key[0]}+{youre_cards_key[1]}={sum_youre_cards} Smaller Than {computer_cards_key[0]}+{computer_cards_key[1]}={sum_comuter_cards} . So You Lose And Computer WIN!😭")

        def calculate_bonus_card(youre_cards=youre_cards, computer_cards=computer_cards):
            '''
            return that the result for choosing the third card!
            :param youre_cards: the value of you're chosen cards.
            :param computer_cards:  the value of computer chosen cards.
            :return: the result
            '''
            bonus_key=list(random.choice(cards).keys())
            for item in cards:
                for key in item:
                    if bonus_key[0]==key:
                        bonus=item[key]

            print(f"you're third card is :{bonus_key}")
            sum_youre_card=bonus+sum(youre_cards)
            sum_computer_cards=sum(computer_cards)
            print(f"sum of you're cards :{youre_cards_key[0]}+{youre_cards_key[1]}+{bonus}={sum_youre_card}")
            print(f"sum of coputer cards :{computer_cards_key[0]}+{computer_cards_key[1]}")
            if sum_youre_card<=21 and sum_youre_card>sum_computer_cards:
                return(f"{sum_youre_card} Bigger Than {sum_computer_cards}. So You WIN!😍")
            elif sum_youre_card<=21 and sum_youre_card == sum_computer_cards:
                return(f"{sum_youre_card} Equal To  {sum_computer_cards}. DRAW!😐")
            elif sum_youre_card>21:
                return(f"the sum of youre cards is Bigger than 21 . So You Lose and Computer WIN!😭")
            elif sum_youre_card<sum_computer_cards:
                return(f"{sum_youre_card} Smaller Than {sum_computer_cards}. So You Lose and Computer WIN!😭")


        if bonus_card=='n':
            print(f"you're cards: {youre_cards_key[0]} , {youre_cards_key[1]}")
            print(f"computer first card :{computer_cards_key[0]}, {computer_cards_key[1]}")
            print(calculate_no_bonus_card())

        elif bonus_card=="y":
            print(calculate_bonus_card())

        end_permission=input("play againg?".title()+"(y/n)\n")

        if end_permission=="y":
            blackjack()
        print('good bye!'.title())


blackjack()


