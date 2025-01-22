import random

from numpy.random import choice

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def selectingCards(n):
    selectedCards=[]
    for i in range(n):
        selectedCards.append(random.choice(cards))

    return selectedCards

def totalSum(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]

    return sum



def blackjack():

    userCards=selectingCards(2)
    computerCards=selectingCards(2)
    print("Your Cards are : ",userCards)
    print("Computer First Card: ",computerCards[0])

    while(True):
        choice = input("Press y to take another card\n"
                       "Press n to call\n"
                       "Choice: ").lower()

        if choice == "y":
            new_card = selectingCards(1)
            if new_card[0]==11 and totalSum(userCards)+totalSum(new_card)>21:
                userCards.append(1)
            userCards.append(new_card[0])
            print("Your Cards are : ", userCards)

        elif choice == "n":
            print("Your final hand is : ", userCards)
            print("Computer final hand is: ",computerCards)

            if totalSum(userCards)>21:
                print("\nYou lose")
                ch=input("press y to play again press n to exit: ")
                if ch=='n':
                    break
                continue
            elif totalSum(userCards)==totalSum(computerCards):
                print("\nTie")
                ch = input("press y to play again press n to exit: ")
                if ch == 'n':
                    break
                continue
            elif totalSum(userCards)>totalSum(computerCards):
                print("\nYou Win")
                ch = input("press y to play again press n to exit: ")
                if ch == 'n':
                    break
                continue
            elif totalSum(computerCards) > totalSum(userCards):
                print("\nYou Lose")
                ch = input("press y to play again press n to exit: ")
                if ch == 'n':
                    break
                continue


if __name__ == '__main__':
    choice = input("Press y to take start the game\n"
                   "Press n to end\n"
                   "Choice: ").lower()

    if choice=='y':
        blackjack()

    print("Exiting")