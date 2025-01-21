import random

word_list = ["ashar","Malik","khan"]

chosen_word = random.choice(word_list)
print(chosen_word)
user_guess = input("Guess a letter: ").lower()

list_of_lines =[]
for i in range(len(chosen_word)):
    list_of_lines.append("_")

# if chosen_word.__contains__(user_guess):
#     print("You have guessed the right letter")
# else:
#     print("Wrong guess")
for i in chosen_word:
    if i==user_guess:
        print("right")
    else:
        print("wrong")


