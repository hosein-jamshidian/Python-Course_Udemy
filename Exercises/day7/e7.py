# # not done

import random
word_list="ardvark baboon camel".split()
chosen_word=random.choice(word_list)

fault=0
display=[]
counter = 0

len_of_chosen_word = len(chosen_word)

for i in range(len_of_chosen_word):
    display.append("_")


while (fault<5) and (counter!=len_of_chosen_word):
    guess=input("please guess a letter :\n").lower()
    s=0

    #guess_index=[]
    for i in range(len_of_chosen_word):
        if chosen_word[i]==guess:
            counter += 1
            #print(counter)
            #print("Right")
            #guess_index.append(i)
            display[i] = chosen_word[i]

        else:
            s=s+1
            #print("Wrong")

    print("".join(display))


    if s==len_of_chosen_word:
        fault+=1
    #print(fault)


print("GAME OVER!")

## FINAL(done):

# the condition for while is diffrent!!
import hangman_arts,hangman_words
import random


print(hangman_arts.logo)
chosen_word=random.choice(hangman_words.word_list)

fault=0
display=[]

len_of_chosen_word = len(chosen_word)

for i in range(len_of_chosen_word):
    display.append("_")

end_of_game=False

while (fault<6) and (end_of_game==False):
    guess=input("please guess a letter :\n").lower()

    if guess in display:
        print(f"you've already guess {guess}.")


    for i in range(len_of_chosen_word):
        if chosen_word[i]==guess:
            display[i] = chosen_word[i]


    if guess not in chosen_word:
        fault += 1
        #print(f"you guess Wrong . you have {6-fault} left")

    print(hangman_arts.hanging_steps[fault])
    print(hangman_arts.comments[fault])

    print("".join(display))


    if "_" not in display:
        end_of_game=True
        print("you WIN!")

print(f"The Real Word Was {chosen_word},GAME OVER!")
