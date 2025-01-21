import random

word_list = ["ashar","Malik","khan"]

chosen_word = random.choice(word_list)

user_guess = input("Guess a letter: ")

if chosen_word.contains(user_guess):
    print("You have guessed the right letter")

