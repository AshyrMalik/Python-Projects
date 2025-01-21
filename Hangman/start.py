import random

word_list = ["ashar","malik","khan"]
hangman_stages = [
    """
      ------
      |    |
           |
           |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
           |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
      |    |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|    |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|\   |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|\   |
     /     |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|\   |
     / \   |
           |
    =========
    """

]



chosen_word = random.choice(word_list)
print(chosen_word)

list_of_lines =[]
for i in range(len(chosen_word)):
    list_of_lines.append("_")

count=0
print(list_of_lines)
lives = 0
while True:
    print(hangman_stages[lives])
    user_guess = input("Guess a letter: ").lower()

    found= False
    for i in chosen_word:
        if i==user_guess:
            list_of_lines[count]=user_guess
            print("right guess")
            print(list_of_lines)
            count+=1
            found=True

    if not found:
        print("wrong guess")
        lives+=1

    if count == len(chosen_word):
        print("You have won")
        break
    if lives==6:
        print(hangman_stages[lives])
        break



