import random

word_list = ["ashar","Malik","khan"]

chosen_word = random.choice(word_list)

# if chosen_word.__contains__(user_guess):
#     print("You have guessed the right letter")
# else:
#     print("Wrong guess")
for i in chosen_word:
    if i==user_guess:
        print("right")
    else:
        print("wrong")


