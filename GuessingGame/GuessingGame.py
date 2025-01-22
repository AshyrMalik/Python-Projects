import random
def GuessingGame():
    choice = input("select difficulty press e for easy\n"
                   "press h for hard ").lower()
    if choice == 'e':
        guess = 10
    guess = 5
    chosen_number =random.randint(1,101)
    guessed = int(input(f"Choose a number between 1 and 100 (You have {guess} guess)"))

    while guess>0:

        if guessed < chosen_number:
            guessed=int(input("Too low try again: "))
            guess-=1
        elif guessed>chosen_number:
            guessed=int(input("Too High try again: "))
            guess -= 1
        else:
            "You have guessed the number Correctly"
            break
    if guess==0:
        print("the number was : ",chosen_number)


if __name__ == '__main__':
    GuessingGame()